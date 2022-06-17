
# DO NOT EDIT THIS FILE -- AUTOGENERATED BY PANTS
# Target: products/datalogue/dtl-python-sdk:dist

from setuptools import setup

setup(**{
    'author': 'Nicolas Joseph',
    'author_email': 'nic@datalogue.io',
    'classifiers': [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
    ],
    'description': 'SDK to interact with the datalogue platform',
    'install_requires': (
        'numpy<2.0,>=1.19.4',
        'pandas<2.0,>=1.1.5',
        'pbkdf2==1.3',
        'pyarrow<9.0,>=8.0.0',
        'python-dateutil<3.0,>=2.8.2',
        'pyyaml<7.0,>=6.0',
        'requests<3.0,>=2.27.1',
        'validators<0.20,>=0.19.0',
    ),
    'license': """
        Copyright 2021 Datalogue, Inc.

        This Datalogue SDK is licensed solely pursuant to the terms of the Master Software License executed between you as Licensee and Datalogue, Inc.

        All rights reserved.
        """,
    'long_description': '',
    'long_description_content_type': 'text/markdown',
    'name': 'datalogue',
    'namespace_packages': (
    ),
    'package_data': {
    },
    'packages': (
        'datalogue',
        'datalogue.auth',
        'datalogue.clients',
        'datalogue.models',
        'datalogue.models.kinesis',
        'datalogue.models.transformations',
    ),
    'python_requires': '>=3.6',
    'setup_requires': [
        'pytest-runner',
    ],
    'tests_require': [
        'pytest>=3.6.3',
        'pytest-cov>=2.6.0',
    ],
    'url': 'https://github.com/datalogue/platform',
    'version': '2022.06.17.1655480975.2516152162',
})
