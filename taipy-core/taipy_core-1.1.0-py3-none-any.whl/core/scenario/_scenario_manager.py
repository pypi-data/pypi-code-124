# Copyright 2022 Avaiga Private Limited
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

import datetime
from functools import partial
from typing import Callable, List, Optional, Union

from taipy.core.common._entity_ids import _EntityIds
from taipy.core.common.alias import ScenarioId
from taipy.core.config.scenario_config import ScenarioConfig
from taipy.core.cycle._cycle_manager_factory import _CycleManagerFactory
from taipy.core.job._job_manager_factory import _JobManagerFactory
from taipy.core.pipeline._pipeline_manager_factory import _PipelineManagerFactory
from taipy.core.scenario._scenario_repository import _ScenarioRepository

from taipy.core._manager._manager import _Manager
from taipy.core.config.config import Config
from taipy.core.cycle.cycle import Cycle
from taipy.core.exceptions.exceptions import (
    DeletingPrimaryScenario,
    DifferentScenarioConfigs,
    DoesNotBelongToACycle,
    InsufficientScenarioToCompare,
    NonExistingComparator,
    NonExistingScenario,
    NonExistingScenarioConfig,
    UnauthorizedTagError,
)
from taipy.core.job.job import Job
from taipy.core.scenario.scenario import Scenario


class _ScenarioManager(_Manager[Scenario]):

    _AUTHORIZED_TAGS_KEY = "authorized_tags"
    _repository = _ScenarioRepository()
    _ENTITY_NAME = Scenario.__name__

    @classmethod
    def _subscribe(
        cls,
        callback: Callable[[Scenario, Job], None],
        params: Optional[List[str]] = None,
        scenario: Optional[Scenario] = None,
    ):
        if scenario is None:
            scenarios = cls._get_all()
            for scn in scenarios:
                cls.__add_subscriber(callback, params, scn)
            return

        cls.__add_subscriber(callback, params, scenario)

    @classmethod
    def _unsubscribe(
        cls,
        callback: Callable[[Scenario, Job], None],
        scenario: Optional[Scenario] = None,
    ):
        if scenario is None:
            scenarios = cls._get_all()
            for scn in scenarios:
                cls.__remove_subscriber(callback, scn)
            return

        cls.__remove_subscriber(callback, scenario)

    @classmethod
    def __add_subscriber(cls, callback, params, scenario):
        scenario._add_subscriber(callback, params)
        cls._set(scenario)

    @classmethod
    def __remove_subscriber(cls, callback, scenario):
        scenario._remove_subscriber(callback)
        cls._set(scenario)

    @classmethod
    def _create(
        cls,
        config: ScenarioConfig,
        creation_date: datetime.datetime = None,
        name: str = None,
    ) -> Scenario:
        scenario_id = Scenario._new_id(config.id)
        pipelines = [
            _PipelineManagerFactory._build_manager()._get_or_create(
                p_config, scenario_id
            )
            for p_config in config.pipeline_configs
        ]
        cycle = (
            _CycleManagerFactory._build_manager()._get_or_create(
                config.frequency, creation_date
            )
            if config.frequency
            else None
        )
        is_primary_scenario = len(cls._get_all_by_cycle(cycle)) == 0 if cycle else False
        props = config._properties.copy()
        if name:
            props["name"] = name
        scenario = Scenario(
            config.id,
            pipelines,  # type: ignore
            props,
            scenario_id,
            creation_date,
            is_primary=is_primary_scenario,
            cycle=cycle,
        )
        cls._set(scenario)
        return scenario

    @classmethod
    def _submit(cls, scenario: Union[Scenario, ScenarioId], force: bool = False):
        scenario_id = scenario.id if isinstance(scenario, Scenario) else scenario
        scenario = cls._get(scenario_id)
        if scenario is None:
            raise NonExistingScenario(scenario_id)
        callbacks = cls.__get_status_notifier_callbacks(scenario)
        for pipeline in scenario.pipelines.values():
            _PipelineManagerFactory._build_manager()._submit(
                pipeline, callbacks=callbacks, force=force
            )

    @classmethod
    def __get_status_notifier_callbacks(cls, scenario: Scenario) -> List:
        return [partial(c.callback, scenario) for c in scenario.subscribers]

    @classmethod
    def _get_primary(cls, cycle: Cycle) -> Optional[Scenario]:
        scenarios = cls._get_all_by_cycle(cycle)
        for scenario in scenarios:
            if scenario.is_primary:
                return scenario
        return None

    @classmethod
    def _get_by_tag(cls, cycle: Cycle, tag: str) -> Optional[Scenario]:
        scenarios = cls._get_all_by_cycle(cycle)
        for scenario in scenarios:
            if scenario.has_tag(tag):
                return scenario
        return None

    @classmethod
    def _get_all_by_tag(cls, tag: str) -> List[Scenario]:
        scenarios = []
        for scenario in cls._get_all():
            if scenario.has_tag(tag):
                scenarios.append(scenario)
        return scenarios

    @classmethod
    def _get_all_by_cycle(cls, cycle: Cycle) -> List[Scenario]:
        return cls._get_all_by(cycle.id)

    @classmethod
    def _get_primary_scenarios(cls) -> List[Scenario]:
        primary_scenarios = []
        for scenario in cls._get_all():
            if scenario.is_primary:
                primary_scenarios.append(scenario)
        return primary_scenarios

    @classmethod
    def _set_primary(cls, scenario: Scenario):
        if scenario.cycle:
            primary_scenario = cls._get_primary(scenario.cycle)
            if primary_scenario:
                primary_scenario._primary_scenario = False
                cls._set(primary_scenario)
            scenario._primary_scenario = True
            cls._set(scenario)
        else:
            raise DoesNotBelongToACycle

    @classmethod
    def _tag(cls, scenario: Scenario, tag: str):
        tags = scenario.properties.get(cls._AUTHORIZED_TAGS_KEY, set())
        if len(tags) > 0 and tag not in tags:
            raise UnauthorizedTagError(
                f"Tag `{tag}` not authorized by scenario configuration `{scenario.config_id}`"
            )
        if scenario.cycle:
            old_tagged_scenario = cls._get_by_tag(scenario.cycle, tag)
            if old_tagged_scenario:
                old_tagged_scenario.remove_tag(tag)
                cls._set(old_tagged_scenario)
        scenario._add_tag(tag)
        cls._set(scenario)

    @classmethod
    def _untag(cls, scenario: Scenario, tag: str):
        scenario._remove_tag(tag)
        cls._set(scenario)

    @classmethod
    def _delete(cls, scenario_id: ScenarioId):  # type: ignore
        if cls._get(scenario_id).is_primary:
            raise DeletingPrimaryScenario
        super()._delete(scenario_id)

    @classmethod
    def _compare(cls, *scenarios: Scenario, data_node_config_id: str = None):
        if len(scenarios) < 2:
            raise InsufficientScenarioToCompare

        if not all(
            [scenarios[0].config_id == scenario.config_id for scenario in scenarios]
        ):
            raise DifferentScenarioConfigs

        if scenario_config := _ScenarioManager.__get_config(scenarios[0]):
            results = {}
            if data_node_config_id:
                if data_node_config_id in scenario_config.comparators.keys():
                    dn_comparators = {
                        data_node_config_id: scenario_config.comparators[
                            data_node_config_id
                        ]
                    }
                else:
                    raise NonExistingComparator
            else:
                dn_comparators = scenario_config.comparators

            for data_node_config_id, comparators in dn_comparators.items():
                data_nodes = [
                    scenario.__getattr__(data_node_config_id).read()
                    for scenario in scenarios
                ]
                results[data_node_config_id] = {
                    comparator.__name__: comparator(*data_nodes)
                    for comparator in comparators
                }

            return results

        else:
            raise NonExistingScenarioConfig(scenarios[0].config_id)

    @staticmethod
    def __get_config(scenario: Scenario):
        return Config.scenarios.get(scenario.config_id, None)

    @classmethod
    def _hard_delete(cls, scenario_id: ScenarioId):
        scenario = cls._get(scenario_id)
        if scenario.is_primary:
            raise DeletingPrimaryScenario
        entity_ids_to_delete = cls._get_owned_entity_ids(scenario)
        entity_ids_to_delete.scenario_ids.add(scenario.id)
        cls._delete_entities_of_multiple_types(entity_ids_to_delete)

    @classmethod
    def _get_owned_entity_ids(cls, scenario: Scenario) -> _EntityIds:
        entity_ids = _EntityIds()

        for pipeline in scenario.pipelines.values():
            if pipeline.parent_id in (pipeline.id, scenario.id):
                entity_ids.pipeline_ids.add(pipeline.id)
            for task in pipeline.tasks.values():
                if task.parent_id in (pipeline.id, scenario.id):
                    entity_ids.task_ids.add(task.id)
                for data_node in task.data_nodes.values():
                    if data_node.parent_id in (pipeline.id, scenario.id):
                        entity_ids.data_node_ids.add(data_node.id)

        jobs = _JobManagerFactory._build_manager()._get_all()
        for job in jobs:
            if job.task.id in entity_ids.task_ids:
                entity_ids.job_ids.add(job.id)

        return entity_ids
