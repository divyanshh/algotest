"""
CoinMarketCapService implements all the apis from CoinMarketCap to get the required data
"""

import requests

from tradesense.dto.crypto_dtos.crypto_dto import CryptoDTO


class CoinMarketCapService:

    def __init__(self, crypto_dto: CryptoDTO):
        self.crypto_dto = crypto_dto

    def get_market_pairs(self):
        url = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/market-pairs/latest?slug={slug}" \
              "&start=1&quoteCurrencyId={quote_currency_id}&limit={limit}&category=spot&centerType=all" \
              "&sort={sort}&direction={direction}".format(slug=self.crypto_dto.slug,
                                                          quote_currency_id=self.crypto_dto.quote_currency_id,
                                                          limit=self.crypto_dto.limit, sort=self.crypto_dto.sort,
                                                          direction=self.crypto_dto.sort_direction)

        payload = {}
        headers = {
            'authority': 'api.coinmarketcap.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-IN,en-US;q=0.9,en;q=0.8,hi-IN;q=0.7,hi;q=0.6,en-GB;q=0.5',
            'cache-control': 'no-cache',
            'dnt': '1',
            'origin': 'https://coinmarketcap.com',
            'platform': 'web',
            'referer': 'https://coinmarketcap.com/',
            'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/115.0.0.0 Safari/537.36',
            'x-request-id': '0ceaf88618924507884ce85bec07e176'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        return response.json()["data"]["marketPairs"]
