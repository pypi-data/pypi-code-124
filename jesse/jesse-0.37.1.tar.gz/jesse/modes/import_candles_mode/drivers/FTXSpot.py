import requests

import jesse.helpers as jh
from jesse.modes.import_candles_mode.drivers.interface import CandleExchange
from jesse.enums import exchanges


class FTXSpot(CandleExchange):
    def __init__(self) -> None:
        # import here instead of the top of the file to prevent the possible circular imports issue
        from jesse.modes.import_candles_mode.drivers.BitfinexSpot import BitfinexSpot

        super().__init__(
            name=exchanges.FTX_SPOT,
            count=1440,
            rate_limit_per_second=6,
            backup_exchange_class=BitfinexSpot
        )

    def get_starting_time(self, symbol: str) -> int:
        formatted_symbol = symbol.replace('-', '/')

        end_timestamp = jh.now()
        start_timestamp = end_timestamp - (86400_000 * 365 * 8)

        payload = {
            'resolution': 86400,
            'start_time': start_timestamp / 1000,
            'end_time': end_timestamp / 1000,
        }

        response = requests.get(
            f'https://ftx.com/api/markets/{formatted_symbol}/candles',
            params=payload
        )

        self.validate_response(response)

        data = response.json()['result']

        # since the first timestamp doesn't include all the 1m
        # candles, let's start since the second day then
        first_timestamp = int(data[0]['time'])
        # second_timestamp:
        return first_timestamp + 60_000 * 1440

    def fetch(self, symbol: str, start_timestamp: int) -> list:
        end_timestamp = start_timestamp + (self.count - 1) * 60000

        payload = {
            'resolution': 60,
            'start_time': start_timestamp / 1000,
            'end_time': end_timestamp / 1000,
        }

        formatted_symbol = symbol.replace('-', '/')

        response = requests.get(
            f'https://ftx.com/api/markets/{formatted_symbol}/candles',
            params=payload
        )

        self.validate_response(response)

        data = response.json()['result']
        return [{
            'id': jh.generate_unique_id(),
            'symbol': symbol,
            'exchange': self.name,
            'timestamp': int(d['time']),
            'open': float(d['open']),
            'close': float(d['close']),
            'high': float(d['high']),
            'low': float(d['low']),
            'volume': float(d['volume'])
        } for d in data]
