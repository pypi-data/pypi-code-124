#!/usr/bin/env python
from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='rxn-opennmt-py',
    description='Fork of OpenNMT-py for use in RXN projects',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='1.1.0',
    packages=find_packages(),
    project_urls={
        "Documentation": "http://opennmt.net/OpenNMT-py/",
        "Forum": "http://forum.opennmt.net/",
        "Gitter": "https://gitter.im/OpenNMT/OpenNMT-py",
        "Source": "https://github.com/OpenNMT/OpenNMT-py/"
    },
    install_requires=[
        "six",
        "tqdm~=4.30.0",
        "torch>=1.2,<1.4", # Originally torch==1.2.0, changed for compatibility with powerai-1.7.0 (pytorch-1.3.1)
        "torchtext==0.4.0",
        "future",
        "configargparse",
    ],
    entry_points={
        "console_scripts": [
            "onmt_server=onmt.bin.server:main",
            "onmt_train=onmt.bin.train:main",
            "onmt_translate=onmt.bin.translate:main",
            "onmt_preprocess=onmt.bin.preprocess:main",
        ],
    }
)
