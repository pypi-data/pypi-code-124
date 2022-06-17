# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['coinmetrics']

package_data = \
{'': ['*']}

install_requires = \
['orjson>=3.6.0,<4.0.0',
 'python-dateutil>=2.8.2,<3.0.0',
 'requests>=2.24.0,<3.0.0',
 'websocket-client>=1.2.1,<2.0.0']

extras_require = \
{'pandas': ['pandas>=1.3.3,<2.0.0']}

entry_points = \
{'console_scripts': ['poetry = poetry.console:run']}

setup_kwargs = {
    'name': 'coinmetrics-api-client',
    'version': '2022.6.17.15.0',
    'description': 'Python client for Coin Metrics API v4.',
    'long_description': '# Coin Metrics Python API v4 client library\n\nThis is an official Python API client for Coin Metrics API v4.\n\n## Installation and Updates\nTo install the client you can run the following command:\n```\npip install coinmetrics-api-client\n```\n\nNote that the client is updated regularly to reflect the changes made in [API v4](https://docs.coinmetrics.io/api/v4). Ensure that your latest version matches with what\'s in [pyPI](https://pypi.org/project/coinmetrics-api-client/) \n\nTo update your version, run the following command:\n```\npip install coinmetrics-api-client -U\n```\n\n## Introduction\nYou can use this client for querying all kinds of data with your API.\n\nTo initialize the client you should use your API key, and the CoinMetricsClient class like the following.\n```\nfrom coinmetrics.api_client import CoinMetricsClient\n\nclient = CoinMetricsClient("<cm_api_key>")\n\n# or to use community API:\nclient = CoinMetricsClient()\n```\n\nAfter that you can use the client object for getting stuff like available markets:\n```\nprint(client.catalog_markets())\n```\n\nor to query all available assets along with what is available for those assets, like metrics, markets:\n\n```\nprint(client.catalog_assets())\n```\n\n\nyou can also use filters for the catalog endpoints like this:\n\n```\nprint(client.catalog_assets(assets=[\'btc\']))\n```\nin this case you would get all the information for btc only\n\nYou can use this client to connect to our API v4 and get catalog or timeseries data from python environment. It natively supports paging over the data so you can use it to iterate over timeseries entries seamlessly.\n\nThe client can be used to query both pro and community data.\n\nThe full list of methods can be found in the [API Client Spec](https://coinmetrics.github.io/api-client-python/site/api_client.html).\n\n## Examples\nThe API Client allows you to chain together workflows for importing, transforming, then exporting Coin Metrics data. Below are examples of common use-cases that can be altered to tailor your specific needs.\n\n**[Example Notebooks](https://github.com/coinmetrics/api-client-python/tree/master/examples/notebooks)**\n\n* `walkthrough_community.ipynb`: Walks through the basic functionality available using the community client.\n\n**[Asset Metrics](https://github.com/coinmetrics/api-client-python/tree/master/examples/asset_metrics)**\n\n* `bbb_metrics_csv_exporter_using_plain_requests.py`: Queries block-by-block metrics using the `requests` library and exports the output into a CSV file.\n* `bbb_metrics_json_exporter.py`: Queries block-by-block metrics and exports the output into a JSON file.\n* `eod_metrics_csv_exporter.py`: Exports a set of user-defined metrics and assets published at end-of-day and exports the output into a CSV file.\n* `reference_rates_json_exporter.py`: Queries Coin Metrics Reference Rates at a user-defined frequency for a set of assets, then exports the output into a JSON file.\n\n**[Market Data](https://github.com/coinmetrics/api-client-python/tree/master/examples/market_data)** \n\n* `books_json_exporter.py`: Queries market orderbook data then exports the output into a JSON file.\n* `candles_json_exporter.py`: Queries market candles data then exports the output into a JSON file.\n* `funding_rates_json_exporter.py`: Queries market funding rates data then exports the output into a JSON file.\n* `trades_csv_exporter.py`: Queries market trades data then exports the output into a CSV file.\n* `trades_json_exporter.py`: Queries market trades data then exports the output into a JSON file.\n\n## Getting timeseries data\n\nFor getting timeseries data you want to use methods of the client class that start with `get_`.\n\nFor example if you want to get a bunch of market data trades for coinbase btc-usd pair you can run something similar to the following:\n\n```\nfor trade in client.get_market_trades(\n    markets=\'coinbase-btc-usd-spot\', \n    start_time=\'2020-01-01\', \n    end_time=\'2020-01-03\',\n    limit_per_market=10\n):\n    print(trade)\n```\n\nOr if you want to see daily btc asset metrics you can use something like this:\n\n```\nfor metric_data in client.get_asset_metrics(assets=\'btc\', \n                                            metrics=[\'ReferenceRateUSD\', \'BlkHgt\', \'AdrActCnt\',  \n                                                     \'AdrActRecCnt\', \'FlowOutBFXUSD\'], \n                                            frequency=\'1d\',\n                                            limit_per_asset=10):\n    print(metric_data)\n```\nThis will print you the requested metrics for all the days where we have any of the metrics present.\n\n\n### DataFrames\n_(New in >=`2021.9.30.14.30`)_\n\nTimeseries data can be transformed into a pandas dataframe by using the `to_dataframe()` method. The code snippet below shows how:\n```\nimport pandas as pd\nfrom coinmetrics.api_client import CoinMetricsClient\nfrom os import environ\n\nclient = CoinMetricsClient()\ntrades = client.get_market_trades(\n    markets=\'coinbase-btc-usd-spot\', \n    start_time=\'2021-09-19T00:00:00Z\', \n    limit_per_market=10\n)\ntrades_df = trades.to_dataframe()\nprint(trades_df.head())\n\n```\nIf you want to use dataframes, then you will need to install pandas\n\n**Notes**\n\n- This only works with requests that return the type `DataCollection`. Thus, `catalog` requests, which return lists cannot be returned as dataframes.\n  Please see the [API Client Spec](https://coinmetrics.github.io/api-client-python/site/api_client.html) for a full list\n  of requests and their return types.\n- API restrictions apply. Some requests may return empty results due to limited access to the API from you API key.\n\n#### Type Conversion \n_(New in >=`2021.12.17.18.00`)_\n\nAs of version `2021.12.17.18.00` or later, outputs from the  `to_dataframe` function automatically convert the dtypes for a dataframe to the optimal pandas types.\n```python\nmetrics_list = [\'volume_trusted_spot_usd_1d\', \'SplyFF\', \'AdrBalUSD1Cnt\']\nasset_list = [\'btc\',\'xmr\']\nstart_time=\'2021-12-01\'\ndf_metrics = client.get_asset_metrics(\n  assets=asset_list, metrics=metrics_list, start_time=start_time, limit_per_asset=3\n).to_dataframe()\nprint(df_metrics.dtypes)\n```\n```\nasset                          string\ntime                           datetime64[ns, tzutc()]\nAdrBalUSD1Cnt                   Int64\nSplyFF                        Float64\nvolume_trusted_spot_usd_1d    Float64\ndtype: object\n```\n\nThis can be turned off by setting `optimize_pandas_types=False`\n\nAlternatively, you can manually enter your own type conversion by passing in a dictionary for `dtype_mapper`. This can be done in conjunction with pandas\' built in type optimizations.\n```python\nmapper = {\n  \'SplyFF\': \'Float64\',\n  \'AdrBalUSD1Cnt\': \'Int64\',\n}\ndf_mapped = client.get_asset_metrics(\n  assets=asset_list, metrics=metrics_list, start_time=start_time, limit_per_asset=3\n).to_dataframe(dtype_mapper=mapper, optimize_pandas_types=True)\nprint(df_mapped.dtypes)\n```\n\n```\nasset                                          object\ntime                          datetime64[ns, tzutc()]\nAdrBalUSD1Cnt                                   Int64\nSplyFF                                        Float64\nvolume_trusted_spot_usd_1d                    float64\ndtype: object\n```\n\nOr as strictly the only types in the dataframe\n\n```python\ndtype_mapper = {\n    \'ReferenceRateUSD\': np.float64,\n    \'time\': np.datetime64\n}\ndf = client.get_asset_metrics(\n  assets=\'btc\', metrics=\'ReferenceRateUSD\', start_time=\'2022-06-15\', limit_per_asset=1\n).to_dataframe(dtype_mapper=dtype_mapper, optimize_pandas_types=False)\ndf.info()\n```\n```\nRangeIndex: 1 entries, 0 to 0\nData columns (total 3 columns):\n #   Column            Non-Null Count  Dtype         \n---  ------            --------------  -----         \n 0   asset             1 non-null      object        \n 1   time              1 non-null      datetime64[ns]\n 2   ReferenceRateUSD  1 non-null      float64       \ndtypes: datetime64[ns](1), float64(1), object(1)\nmemory usage: 152.0+ bytes\n```\n\nNote that in order to pass a custom datetime object, setting a dtype_mapper is mandatory.\n\nPandas type conversion tends to be more performant. But if there are custom operations that must be done using numpy datatypes, this option will let you perform them.\n\n### Paging\nYou can make the datapoints to iterate from start or from end (default).\n\nfor that you should use a paging_from argument like the following:\n```\nfrom coinmetrics.api_client import CoinMetricsClient\nfrom coinmetrics.constants import PagingFrom\n\nclient = CoinMetricsClient()\n\nfor metric_data in client.get_asset_metrics(assets=\'btc\', metrics=[\'ReferenceRateUSD\'],\n                                            paging_from=PagingFrom.START):\n    print(metric_data)\n```\n\nPagingFrom.END: is available but it is also a default value also, so you might not want to set it.\n\n### SSL Certs verification\n\nSometimes your organization network have special rules on SSL certs verification and in this case you might face the following error when running the script:\n```text\nSSLError: HTTPSConnectionPool(host=\'api.coinmetrics.io\', port=443): Max retries exceeded with url: <some_url_path> (Caused by SSLError(SSLCertVerificationError(1, \'[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain (_ssl.c:1123)\')))\n```\n\nIn this case, you can pass an option during client initialization to disable ssl verification for requests like this:\n\n```python\n\nclient = CoinMetricsClient(verify_ssl_certs=False)\n```\n\nWe don\'t recommend setting it to False by default and you should make sure you understand the security risks of disabling SSL certs verification.\n\n\n### Requests Proxy\nSometimes your organization has special rules on making requests to third parties and you have to use proxies in order to comply with the rules.\n\nFor proxies that don\'t require auth you can specify them similar to this example:\n```python\n\nclient = CoinMetricsClient(proxy_url=f\'http://<hostname>:<port>\')\n```\n\nFor proxies that require auth, you should be able to specify username and password similar to this example:\n```python\n\nclient = CoinMetricsClient(proxy_url=f\'http://<username>:<password>@<hostname>:<port>\')\n```\n\n## Extended documentation\nFor more information about the available methods in the client please reference [API Client Spec](https://coinmetrics.github.io/api-client-python/site/api_client.html)\n',
    'author': 'Coin Metrics',
    'author_email': 'info@coinmetrics.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://coinmetrics.github.io/api-client-python/site/index.html',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
