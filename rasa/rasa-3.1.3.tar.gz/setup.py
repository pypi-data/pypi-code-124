# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rasa',
 'rasa.cli',
 'rasa.cli.arguments',
 'rasa.cli.initial_project.actions',
 'rasa.core',
 'rasa.core.actions',
 'rasa.core.brokers',
 'rasa.core.channels',
 'rasa.core.evaluation',
 'rasa.core.featurizers',
 'rasa.core.nlg',
 'rasa.core.policies',
 'rasa.core.training',
 'rasa.core.training.converters',
 'rasa.engine',
 'rasa.engine.recipes',
 'rasa.engine.runner',
 'rasa.engine.storage',
 'rasa.engine.training',
 'rasa.graph_components',
 'rasa.graph_components.converters',
 'rasa.graph_components.providers',
 'rasa.graph_components.validators',
 'rasa.nlu',
 'rasa.nlu.classifiers',
 'rasa.nlu.emulators',
 'rasa.nlu.extractors',
 'rasa.nlu.featurizers',
 'rasa.nlu.featurizers.dense_featurizer',
 'rasa.nlu.featurizers.sparse_featurizer',
 'rasa.nlu.selectors',
 'rasa.nlu.tokenizers',
 'rasa.nlu.utils',
 'rasa.nlu.utils.hugging_face',
 'rasa.shared',
 'rasa.shared.core',
 'rasa.shared.core.training_data',
 'rasa.shared.core.training_data.story_reader',
 'rasa.shared.core.training_data.story_writer',
 'rasa.shared.importers',
 'rasa.shared.nlu',
 'rasa.shared.nlu.training_data',
 'rasa.shared.nlu.training_data.formats',
 'rasa.shared.nlu.training_data.schemas',
 'rasa.shared.utils',
 'rasa.shared.utils.schemas',
 'rasa.utils',
 'rasa.utils.tensorflow']

package_data = \
{'': ['*'],
 'rasa.cli': ['initial_project/*',
              'initial_project/data/*',
              'initial_project/tests/*'],
 'rasa.engine.recipes': ['config_files/*']}

install_requires = \
['CacheControl>=0.12.9,<0.13.0',
 'PyJWT[crypto]>=2.0.0,<3.0.0',
 'SQLAlchemy>=1.4.0,<1.5.0',
 'absl-py>=0.9,<0.14',
 'aio-pika>=6.7.1,<7.0.0',
 'aiohttp>=3.6,<3.8,!=3.7.4.post0',
 'apscheduler>=3.6,<3.8',
 'async_generator>=1.10,<1.11',
 'attrs>=19.3,<21.3',
 'boto3>=1.12,<2.0',
 'cloudpickle>=1.2,<1.7',
 'colorclass>=2.2,<2.3',
 'coloredlogs>=10,<16',
 'colorhash>=1.0.2,<1.1.0',
 'dask==2021.11.2',
 'fbmessenger>=6.0.0,<6.1.0',
 'google-auth<2',
 'joblib>=0.15.1,<1.1.0',
 'jsonpickle>=1.3,<2.1',
 'jsonschema>=3.2,<3.3',
 'kafka-python>=1.4,<3.0',
 'matplotlib>=3.1,<3.4',
 'mattermostwrapper>=2.2,<2.3',
 'networkx>=2.4,<2.7',
 'numpy>=1.19.2,<1.20.0',
 'packaging>=20.0,<21.0',
 'prompt-toolkit>=2.0,<3.0',
 'psycopg2-binary>=2.8.2,<2.10.0',
 'pyTelegramBotAPI>=3.7.3,<4.0.0',
 'pydot>=1.4,<1.5',
 'pykwalify>=1.7,<1.9',
 'pymongo[srv,tls]>=3.8,<3.11',
 'python-dateutil>=2.8,<2.9',
 'python-engineio>=4,<6,!=5.0.0',
 'python-socketio>=4.4,<6',
 'pytz>=2019.1,<2022.0',
 'questionary>=1.5.1,<1.11.0',
 'randomname>=0.1.5,<0.2.0',
 'rasa-sdk>=3.1.1,<3.2.0',
 'redis>=3.4,<4.0',
 'regex>=2020.6,<2021.9',
 'requests>=2.23,<3.0',
 'rocketchat_API>=0.6.31,<1.17.0',
 'ruamel.yaml>=0.16.5,<0.17.0',
 'sanic-cors>=2.0.0,<3.0.0',
 'sanic-jwt>=1.6.0,<2.0.0',
 'sanic-routing>=0.7.2,<0.8.0',
 'sanic>=21.12,<21.13',
 'scikit-learn>=0.22,<0.25',
 'scipy>=1.4.1,<1.8.0',
 'sentry-sdk>=0.17.0,<1.4.0',
 'setuptools>=41.0.0',
 'sklearn-crfsuite>=0.3,<0.4',
 'slackclient>=2.0.0,<3.0.0',
 'tarsafe>=0.0.3,<0.0.4',
 'tensorflow-addons>=0.15.0,<0.16.0',
 'tensorflow>=2.7.0,<2.8.0',
 'tensorflow_hub>=0.12.0,<0.13.0',
 'terminaltables>=3.1.0,<3.2.0',
 'tqdm>=4.31,<5.0',
 'twilio>=6.26,<6.51',
 'typing-extensions>=3.7.4,<4.0.0',
 'typing-utils>=0.1.0,<0.2.0',
 'ujson>=1.35,<5.0',
 'webexteamssdk>=1.1.1,<1.7.0']

extras_require = \
{':sys_platform != "win32"': ['tensorflow-text>=2.7.0,<3.0.0'],
 ':sys_platform == "win32"': ['colorama>=0.4.4,<0.5.0'],
 'full': ['spacy>=3.1,<4.0',
          'transformers>=4.13.0,<4.14.0',
          'sentencepiece[sentencepiece]>=0.1.96,<0.2.0',
          'jieba>=0.39,<0.43'],
 'gh-release-notes': ['github3.py>=1.3.0,<1.4.0'],
 'jieba': ['jieba>=0.39,<0.43'],
 'spacy': ['spacy>=3.1,<4.0'],
 'transformers': ['transformers>=4.13.0,<4.14.0',
                  'sentencepiece[sentencepiece]>=0.1.96,<0.2.0']}

entry_points = \
{'console_scripts': ['rasa = rasa.__main__:main']}

setup_kwargs = {
    'name': 'rasa',
    'version': '3.1.3',
    'description': 'Open source machine learning framework to automate text- and voice-based conversations: NLU, dialogue management, connect to Slack, Facebook, and more - Create chatbots and voice assistants',
    'long_description': '<h1 align="center">Rasa Open Source</h1>\n\n<div align="center">\n\n[![Join the chat on Rasa Community Forum](https://img.shields.io/badge/forum-join%20discussions-brightgreen.svg)](https://forum.rasa.com/?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)\n[![PyPI version](https://badge.fury.io/py/rasa.svg)](https://badge.fury.io/py/rasa)\n[![Supported Python Versions](https://img.shields.io/pypi/pyversions/rasa.svg)](https://pypi.python.org/pypi/rasa)\n[![Build Status](https://github.com/RasaHQ/rasa/workflows/Continuous%20Integration/badge.svg)](https://github.com/RasaHQ/rasa/actions)\n[![Coverage Status](https://coveralls.io/repos/github/RasaHQ/rasa/badge.svg?branch=main)](https://coveralls.io/github/RasaHQ/rasa?branch=main)\n[![Documentation Status](https://img.shields.io/badge/docs-stable-brightgreen.svg)](https://rasa.com/docs)\n![Documentation Build](https://img.shields.io/netlify/d2e447e4-5a5e-4dc7-be5d-7c04ae7ff706?label=Documentation%20Build)\n[![FOSSA Status](https://app.fossa.com/api/projects/custom%2B8141%2Fgit%40github.com%3ARasaHQ%2Frasa.git.svg?type=shield)](https://app.fossa.com/projects/custom%2B8141%2Fgit%40github.com%3ARasaHQ%2Frasa.git?ref=badge_shield)\n[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/orgs/RasaHQ/projects/23)\n\n</div>\n\n<a href="https://grnh.se/05a908c02us" target="_blank"><img align="center" src="https://www.rasa.com/assets/img/github/hiring_banner.png" alt="An image with Sara, the Rasa mascot, standing next to a roadmap with future Rasa milestones: identifying unsuccessful conversations at scale, continuous model evaluation, controllable NLG and breaking free from intents. Are you excited about these milestones? Help us make these ideas become reality - we\'re hiring!" title="We\'re hiring! Learn more"></a>\n\n<hr />\n\n💡 **Rasa Open Source 3.0 is here!** 💡\n\n[2.8](https://github.com/RasaHQ/rasa/milestone/39) is the last minor in the 2.x series.\nYou can still contribute new features and improvements which we plan to release alongside\nupdates to 3.0. Read more about [our contributor guidelines](#how-to-contribute).\n\n<hr />\n\n<img align="right" height="244" src="https://www.rasa.com/assets/img/sara/sara-open-source-2.0.png" alt="An image of Sara, the Rasa mascot bird, holding a flag that reads Open Source with one wing, and a wrench in the other" title="Rasa Open Source">\n\nRasa is an open source machine learning framework to automate text-and voice-based conversations. With Rasa, you can build contextual assistants on:\n- Facebook Messenger\n- Slack\n- Google Hangouts\n- Webex Teams\n- Microsoft Bot Framework\n- Rocket.Chat\n- Mattermost\n- Telegram\n- Twilio\n- Your own custom conversational channels\n\nor voice assistants as:\n- Alexa Skills\n- Google Home Actions\n\nRasa helps you build contextual assistants capable of having layered conversations with\nlots of back-and-forth. In order for a human to have a meaningful exchange with a contextual\nassistant, the assistant needs to be able to use context to build on things that were previously\ndiscussed – Rasa enables you to build assistants that can do this in a scalable way.\n\nThere\'s a lot more background information in this\n[blog post](https://medium.com/rasa-blog/a-new-approach-to-conversational-software-2e64a5d05f2a).\n\n---\n- **What does Rasa do? 🤔**\n  [Check out our Website](https://rasa.com/)\n\n- **I\'m new to Rasa 😄**\n  [Get Started with Rasa](https://rasa.com/docs/getting-started/)\n\n- **I\'d like to read the detailed docs 🤓**\n  [Read The Docs](https://rasa.com/docs/)\n\n- **I\'m ready to install Rasa 🚀**\n  [Installation](https://rasa.com/docs/rasa/user-guide/installation/)\n\n- **I want to learn how to use Rasa 🚀**\n  [Tutorial](https://rasa.com/docs/rasa/user-guide/rasa-tutorial/)\n\n- **I have a question ❓**\n  [Rasa Community Forum](https://forum.rasa.com/)\n\n- **I would like to contribute 🤗**\n  [How to Contribute](#how-to-contribute)\n\n---\n## Where to get help\n\nThere is extensive documentation in the [Rasa Docs](https://rasa.com/docs/rasa).\nMake sure to select the correct version so you are looking at\nthe docs for the version you installed.\n\nPlease use [Rasa Community Forum](https://forum.rasa.com) for quick answers to\nquestions.\n\n### README Contents:\n- [How to contribute](#how-to-contribute)\n- [Development Internals](#development-internals)\n- [Releases](#releases)\n- [License](#license)\n\n### How to contribute\nWe are very happy to receive and merge your contributions into this repository!\n\nTo contribute via pull request, follow these steps:\n\n1. Create an issue describing the feature you want to work on (or\n   have a look at the [contributor board](https://github.com/orgs/RasaHQ/projects/23))\n2. Write your code, tests and documentation, and format them with ``black``\n3. Create a pull request describing your changes\n\nFor more detailed instructions on how to contribute code, check out these [code contributor guidelines](CONTRIBUTING.md).\n\nYou can find more information about how to contribute to Rasa (in lots of\ndifferent ways!) [on our website.](http://rasa.com/community/contribute).\n\nYour pull request will be reviewed by a maintainer, who will get\nback to you about any necessary changes or questions. You will\nalso be asked to sign a\n[Contributor License Agreement](https://cla-assistant.io/RasaHQ/rasa).\n\n\n## Development Internals\n\n### Installing Poetry\n\nRasa uses Poetry for packaging and dependency management. If you want to build it from source,\nyou have to install Poetry first. This is how it can be done:\n\n```bash\ncurl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python\n```\n\nThere are several other ways to install Poetry. Please, follow\n[the official guide](https://python-poetry.org/docs/#installation) to see all possible options.\n\n### Managing environments\n\nThe official [Poetry guide](https://python-poetry.org/docs/managing-environments/) suggests to use\n[pyenv](https://github.com/pyenv/pyenv) or any other similar tool to easily switch between Python versions.\nThis is how it can be done:\n\n```bash\npyenv install 3.7.9\npyenv local 3.7.9  # Activate Python 3.7.9 for the current project\n```\n*Note*: If you have trouble installing a specific version of python on your system\nit might be worth trying other supported versions.\n\nBy default, Poetry will try to use the currently activated Python version to create the virtual environment\nfor the current project automatically. You can also create and activate a virtual environment manually — in this\ncase, Poetry should pick it up and use it to install the dependencies. For example:\n\n```bash\npython -m venv .venv\nsource .venv/bin/activate\n```\n\nYou can make sure that the environment is picked up by executing\n\n```bash\npoetry env info\n```\n\n### Building from source\n\nTo install dependencies and `rasa` itself in editable mode execute\n\n```bash\nmake install\n```\n\n*Note for macOS users*: under macOS Big Sur we\'ve seen some compiler issues for \ndependencies. Using `export SYSTEM_VERSION_COMPAT=1` before the installation helped. \n\n### Running and changing the documentation\n\nFirst of all, install all the required dependencies:\n\n```bash\nmake install install-docs\n```\n\nAfter the installation has finished, you can run and view the documentation\nlocally using:\n\n```bash\nmake livedocs\n```\n\nIt should open a new tab with the local version of the docs in your browser;\nif not, visit http://localhost:3000 in your browser.\nYou can now change the docs locally and the web page will automatically reload\nand apply your changes.\n\n### Running the Tests\n\nIn order to run the tests, make sure that you have the development requirements installed:\n\n```bash\nmake prepare-tests-ubuntu # Only on Ubuntu and Debian based systems\nmake prepare-tests-macos  # Only on macOS\n```\n\nThen, run the tests:\n\n```bash\nmake test\n```\n\nThey can also be run at multiple jobs to save some time:\n\n```bash\nJOBS=[n] make test\n```\n\nWhere `[n]` is the number of jobs desired. If omitted, `[n]` will be automatically chosen by pytest.\n\n\n### Running the Integration Tests\n\nIn order to run the integration tests, make sure that you have the development requirements installed:\n\n```bash\nmake prepare-tests-ubuntu # Only on Ubuntu and Debian based systems\nmake prepare-tests-macos  # Only on macOS\n```\n\nThen, you\'ll need to start services with the following command which uses\n[Docker Compose](https://docs.docker.com/compose/install/):\n\n```bash\nmake run-integration-containers\n```\n\nFinally, you can run the integration tests like this:\n\n```bash\nmake test-integration\n```\n\n\n### Resolving merge conflicts\n\nPoetry doesn\'t include any solution that can help to resolve merge conflicts in\nthe lock file `poetry.lock` by default.\nHowever, there is a great tool called [poetry-merge-lock](https://poetry-merge-lock.readthedocs.io/en/latest/).\nHere is how you can install it:\n\n```bash\npip install poetry-merge-lock\n```\n\nJust execute this command to resolve merge conflicts in `poetry.lock` automatically:\n\n```bash\npoetry-merge-lock\n```\n\n### Build a Docker image locally\n\nIn order to build a Docker image on your local machine execute the following command:\n\n```bash\nmake build-docker\n```\n\nThe Docker image is available on your local machine as `rasa:localdev`.\n\n### Code Style\n\nTo ensure a standardized code style we use the formatter [black](https://github.com/ambv/black).\nTo ensure our type annotations are correct we use the type checker [pytype](https://github.com/google/pytype).\nIf your code is not formatted properly or doesn\'t type check, GitHub will fail to build.\n\n#### Formatting\n\nIf you want to automatically format your code on every commit, you can use [pre-commit](https://pre-commit.com/).\nJust install it via `pip install pre-commit` and execute `pre-commit install` in the root folder.\nThis will add a hook to the repository, which reformats files on every commit.\n\nIf you want to set it up manually, install black via `poetry install`.\nTo reformat files execute\n```\nmake formatter\n```\n\n#### Type Checking\n\nIf you want to check types on the codebase, install `mypy` using `poetry install`.\nTo check the types execute\n```\nmake types\n```\n\n### Deploying documentation updates\n\nWe use `Docusaurus v2` to build docs for tagged versions and for the `main` branch.\nThe static site that gets built is pushed to the `documentation` branch of this repo.\n\nWe host the site on netlify. On `main` branch builds (see `.github/workflows/documentation.yml`), we push the built docs to\nthe `documentation` branch. Netlify automatically re-deploys the docs pages whenever there is a change to that branch.\n\n## Releases\n### Release Timeline for Minor Releases\n**For Rasa Open Source, we usually commit to time-based releases, specifically on a monthly basis.**\nThis means that we commit beforehand to releasing a specific version of Rasa Open Source on a specific day,\nand we cannot be 100% sure what will go in a release, because certain features may not be ready.\n\nAt the beginning of each quarter, the Rasa team will review the scheduled release dates for all products and make sure\nthey work for the projected work we have planned for the quarter, as well as work well across products.\n\n**Once the dates are settled upon, we update the respective [milestones](https://github.com/RasaHQ/rasa/milestones).**\n\n### Cutting a Major / Minor release\n#### A week before release day\n\n1. **Make sure the [milestone](https://github.com/RasaHQ/rasa/milestones) already exists and is scheduled for the\ncorrect date.**\n2. **Take a look at the issues & PRs that are in the milestone**: does it look about right for the release highlights\nwe are planning to ship? Does it look like anything is missing? Don\'t worry about being aware of every PR that should\nbe in, but it\'s useful to take a moment to evaluate what\'s assigned to the milestone.\n3. **Post a message on the engineering Slack channel**, letting the team know you\'ll be the one cutting the upcoming\nrelease, as well as:\n    1. Providing the link to the appropriate milestone\n    2. Reminding everyone to go over their issues and PRs and please assign them to the milestone\n    3. Reminding everyone of the scheduled date for the release\n\n#### A day before release day\n\n1. **Go over the milestone and evaluate the status of any PR merging that\'s happening. Follow up with people on their\nbugs and fixes.** If the release introduces new bugs or regressions that can\'t be fixed in time, we should discuss on\nSlack about this and take a decision on how to move forward. If the issue is not ready to be merged in time, we remove the issue / PR from the milestone and notify the PR owner and the product manager on Slack about it. The PR / issue owners are responsible for\ncommunicating any issues which might be release relevant. Postponing the release should be considered as an edge case scenario.\n\n#### Release day! 🚀\n\n1. **At the start of the day, post a small message on slack announcing release day!** Communicate you\'ll be handling\nthe release, and the time you\'re aiming to start releasing (again, no later than 4pm, as issues may arise and\ncause delays). This message should be posted early in the morning and before moving forward with any of the steps of the release, \n   in order to give enough time to people to check their PRs and issues. That way they can plan any remaining work. A template of the slack message can be found [here](https://rasa-hq.slack.com/archives/C36SS4N8M/p1613032208137500?thread_ts=1612876410.068400&cid=C36SS4N8M).\n   The release time should be communicated transparently so that others can plan potentially necessary steps accordingly. If there are bigger changes this should be communicated.\n2. Make sure the milestone is empty (everything has been either merged or moved to the next milestone)\n3. Once everything in the milestone is taken care of, post a small message on Slack communicating you are about to\nstart the release process (in case anything is missing).\n4. **You may now do the release by following the instructions outlined in the\n[Rasa Open Source README](#steps-to-release-a-new-version) !**\n\n#### After a Major release\n\nAfter a Major release has been completed, please follow [these instructions to complete the documentation update](./docs/README.md#manual-steps-after-a-new-version).\n\n### Steps to release a new version\nReleasing a new version is quite simple, as the packages are build and distributed by GitHub Actions.\n\n*Terminology*:\n* micro release (third version part increases): 1.1.2 -> 1.1.3\n* minor release (second version part increases): 1.1.3 -> 1.2.0\n* major release (first version part increases): 1.2.0 -> 2.0.0\n\n*Release steps*:\n1. Make sure all dependencies are up to date (**especially Rasa SDK**)\n    - For Rasa SDK, except in the case of a micro release, that means first creating a [new Rasa SDK release](https://github.com/RasaHQ/rasa-sdk#steps-to-release-a-new-version) (make sure the version numbers between the new Rasa and Rasa SDK releases match)\n    - Once the tag with the new Rasa SDK release is pushed and the package appears on [pypi](https://pypi.org/project/rasa-sdk/), the dependency in the rasa repository can be resolved (see below).\n2. In case of a minor release, create a new branch that corresponds to the new release, e.g. \n   ```bash\n    git checkout -b 1.2.x\n    git push origin 1.2.x\n    ```\n3. Switch to the branch you want to cut the release from (`main` in case of a major, the `<major>.<minor>.x` branch for minors and micros)\n    - Update the `rasa-sdk` entry in `pyproject.toml` with the new release version and run `poetry update`. This creates a new `poetry.lock` file with all dependencies resolved.\n    - Commit the changes with `git commit -am "bump rasa-sdk dependency"` but do not push them. They will be automatically picked up by the following step.\n4. If this is a major release, update the list of actively maintained versions [in the README](#actively-maintained-versions) and in [the docs](./docs/docs/actively-maintained-versions.mdx).\n5. Run `make release`\n6. Create a PR against the release branch (e.g. `1.2.x`)\n7. Once your PR is merged, tag a new release (this SHOULD always happen on the release branch), e.g. using\n    ```bash\n    git checkout 1.2.x\n    git pull origin 1.2.x\n    git tag 1.2.0 -m "next release"\n    git push origin 1.2.0 --tags\n    ```\n    GitHub will build this tag and publish the build artifacts.\n8. After all the steps are completed and if everything goes well then we should see a message automatically posted in the company\'s Slack (`product` channel) like this [one](https://rasa-hq.slack.com/archives/C7B08Q5FX/p1614354499046600)\n9. If no message appears in the channel then you can do the following checks:\n    - Check the workflows in [Github Actions](https://github.com/RasaHQ/rasa/actions) and make sure that the merged PR of the current release is completed successfully. To easily find your PR you can use the filters `event: push` and `branch: <version number>` (example on release 2.4 you can see [here](https://github.com/RasaHQ/rasa/actions/runs/643344876))\n    - If the workflow is not completed, then try to re run the workflow in case that solves the problem\n    - If the problem persists, check also the log files and try to find the root cause of the issue\n    - If you still cannot resolve the error, contact the infrastructure team by providing any helpful information from your investigation\n10.  After the message is posted correctly in the `product` channel, check also in the `product-engineering-alerts` channel if there are any alerts related to the Rasa Open Source release like this [one](https://rasa-hq.slack.com/archives/C01585AN2NP/p1615486087001000)\n    \n### Cutting a Micro release\n\nMicro releases are simpler to cut, since they are meant to contain only bugfixes.\n\n**The only things you need to do to cut a micro are:**\n\n1. Notify the engineering team on Slack that you are planning to cut a micro, in case someone has an important fix\nto add.\n2. Make sure the bugfix(es) are in the release branch you will use (p.e if you are cutting a `2.0.4` micro, you will\nneed your fixes to be on the `2.0.x` release branch). All micros must come from a `.x` branch!\n3. Once you\'re ready to release the Rasa Open Source micro, checkout the branch, run `make release` and follow the\nsteps + get the PR merged.\n4. Once the PR is in, pull the `.x` branch again and push the tag!\n\n### Actively maintained versions\n\nWe\'re actively maintaining _any minor on our latest major release_ and _the latest minor of the previous major release_.\nCurrently, this means the following minor versions will receive bugfixes updates:\n- 2.8\n- Every minor version on 3.x\n\n## License\nLicensed under the Apache License, Version 2.0.\nCopyright 2021 Rasa Technologies GmbH. [Copy of the license](LICENSE.txt).\n\nA list of the Licenses of the dependencies of the project can be found at\nthe bottom of the\n[Libraries Summary](https://libraries.io/github/RasaHQ/rasa).\n',
    'author': 'Rasa Technologies GmbH',
    'author_email': 'hi@rasa.com',
    'maintainer': 'Tom Bocklisch',
    'maintainer_email': 'tom@rasa.com',
    'url': 'https://rasa.com',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<3.10',
}


setup(**setup_kwargs)
