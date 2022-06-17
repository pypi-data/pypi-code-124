from __future__ import annotations

import collections
from math import ceil
from typing import (Deque, Dict, FrozenSet, Generic, Mapping, Optional,
                    Sequence, Tuple)
from uuid import uuid4

import instancelib as il
import numpy as np
from instancelib.ingest.qrel import TrecDataset
from instancelib.typehints import DT, KT, LT, RT, VT

from ..analysis.base import (AbstractStatistics, AnnotationStatistics,
                             StatsMixin)
from ..analysis.initialization import Initializer
from ..environment.base import AbstractEnvironment
from ..typehints import IT
from ..utils.func import list_unzip, sort_on
from ..utils.numpy import raw_proba_chainer
from .base import ActiveLearner
from .poolbased import PoolBasedAL

PSEUDO_INS_PROVIDER = "PSEUDO_INSTANCES"

class PseudoInstanceInitializer(Initializer[IT, KT, LT], 
                                Generic[IT, KT, DT, LT]):
    def __init__(self, pseudo_data: DT, pseudo_label: LT):
        self.pseudo_data = pseudo_data
        self.pseudo_label = pseudo_label
        self.pseudo_id = uuid4()

    def __call__(self, 
                 learner: ActiveLearner[IT, KT, DT, VT, RT, LT]
                 ) -> ActiveLearner[IT, KT, DT, VT, RT, LT]:
        ins = learner.env.create(data=self.pseudo_data, vector=None)
        learner.env.create_named_provider(PSEUDO_INS_PROVIDER, [ins.identifier])
        return learner 
    
    @classmethod
    def from_trec(cls, trec: TrecDataset, topic_id: str) -> PseudoInstanceInitializer[IT, str, str, str]:
        topic_df = trec.topics.set_index("id")
        topic_row = topic_df.xs(topic_id)
        pseudo_data: str = topic_row.title + " " + topic_row.query
        return cls(pseudo_data, trec.pos_label) # type: ignore



class AutoTarLearner(PoolBasedAL[IT, KT, DT, VT, RT, LT], 
                     StatsMixin[KT, LT],
                     Generic[IT, KT, DT, VT, RT, LT]):
    rank_history: Dict[int, Mapping[KT, int]]
    sampled_sets: Dict[int, Sequence[KT]]
    batch_sizes:  Dict[int, int]
    current_sample: Deque[KT]
    rng: np.random.Generator
    _stats: AbstractStatistics[KT, LT]

    def __init__(self, 
                 classifier: il.AbstractClassifier[IT, KT, DT, VT, RT, LT, np.ndarray, np.ndarray],
                 pos_label: LT, 
                 neg_label: LT, 
                 k_sample: int,
                 batch_size: int,
                 *_, 
                 seed: int = 0,  
                 identifier: Optional[str] = None, 
                 **__) -> None:
        super().__init__(*_, identifier=identifier, **__)
        # Problem definition
        self.classifier = classifier
        self.pos_label = pos_label
        self.neg_label = neg_label

        # Batch and sample sizes
        self.k_sample = k_sample
        self.batch_sizes = dict()
        self.batch_size = batch_size
        
        # Record keeping for the current sample
        self.it = 0
        self.current_sample = collections.deque()
        self.batch_sizes[self.it] = batch_size

        # Record keeping for recall analysis
        self.rank_history = dict()
        self.sampled_sets = dict()

        # Random generator for sampling
        self.rng = np.random.default_rng(seed)

        # Statistics Logger for Stopping
        self._stats = AnnotationStatistics()
        
    @property
    def stats(self) -> AbstractStatistics[KT, LT]:
        return self._stats 

    def __call__(self, environment: AbstractEnvironment[IT, KT, DT, VT, RT, LT]) -> PoolBasedAL[IT, KT, DT, VT, RT, LT]:
        super().__call__(environment)
        self.classifier.set_target_labels(self.env.labels.labelset)
        return self

    def update_ordering(self) -> bool:
        return True

    def _provider_sample(self, provider: il.InstanceProvider[IT, KT, DT, VT, RT]) -> il.InstanceProvider[IT, KT, DT, VT, RT]:
        k_sample = min(self.k_sample, len(provider))
        sampled_keys: Sequence[KT] = self.rng.choice(
            provider.key_list, 
            size=k_sample, replace=False).tolist()
        sampled_provider = self.env.create_bucket(sampled_keys)
        return sampled_provider

    def _temp_augment_and_train(self):
        temp_labels = il.MemoryLabelProvider.from_provider(self.env.labels)
        sampled_non_relevant = self._provider_sample(self.env.unlabeled)
        if PSEUDO_INS_PROVIDER in self.env:
            pseudo_docs = self.env[PSEUDO_INS_PROVIDER]
            for ins_key in pseudo_docs:
                temp_labels.set_labels(ins_key, self.pos_label)
        else:
            pseudo_docs = self.env.create_bucket([])
        for ins_key in sampled_non_relevant:
            temp_labels.set_labels(ins_key, self.neg_label)
        train_set = self.env.combine(sampled_non_relevant, self.env.labeled, pseudo_docs)
        self.classifier.fit_provider(train_set, temp_labels)

    def _predict(self, provider: il.InstanceProvider[IT, KT, DT, VT, RT]) -> Tuple[Sequence[KT], np.ndarray]:
        raw_probas = self.classifier.predict_proba_provider_raw(provider)
        keys, matrix = raw_proba_chainer(raw_probas)
        return keys, matrix

    def _rank(self, provider: il.InstanceProvider[IT, KT, DT, VT, RT]) -> Sequence[Tuple[KT, float]]:
        keys, matrix = self._predict(provider)
        pos_column = self.classifier.get_label_column_index(self.pos_label)
        prob_vector = matrix[:,pos_column]
        floats: Sequence[float] = prob_vector.tolist()
        zipped = list(zip(keys, floats))
        ranking = sort_on(1, zipped)
        return ranking

    def _sample(self, distribution: Sequence[Tuple[KT, float]]) -> Sequence[KT]:
        keys, _ = list_unzip(distribution)
        sample = keys[0:self.batch_size]
        return sample

    @classmethod
    def _to_history(cls, ranking: Sequence[Tuple[KT, float]]) -> Mapping[KT, int]:
        keys, _ = list_unzip(ranking)
        history = {k: i for i, k in enumerate(keys, start=1)}
        return history

    def update_sample(self) -> Deque[KT]:
        if not self.current_sample:
            self.stats.update(self)
            self._temp_augment_and_train()
            ranking = self._rank(self.env.unlabeled)
            sample = self._sample(ranking)
            
            # Store current sample
            self.current_sample = collections.deque(sample)
            
            # Record keeping
            self.rank_history[self.it] = self._to_history(ranking)
            self.sampled_sets[self.it] = tuple(sample)
            self.batch_sizes[self.it] = self.batch_size

            # Increment batch_size for next for train iteration
            self.batch_size += ceil(self.batch_size / 10)
            self.it+= 1
        return self.current_sample
        
    def __next__(self) -> IT:
        self.update_sample()
        while self.current_sample:
            ins_key = self.current_sample.popleft()
            if ins_key not in self.env.labeled:
                return self.env.dataset[ins_key]
        if not self.env.unlabeled.empty:
            return self.__next__()
        raise StopIteration()
            
            
            

            

                
        