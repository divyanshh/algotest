"""
TradeSenseService
"""
from traderx.tradesense.services.arbitrage_service import ArbitrageService
from traderx.tradesense.services.coinmarketcap_service import CoinMarketCapService
from traderx.tradesense.services.crypto_dtos.bitcoin_dto import BitcoinDTO
from traderx.tradesense.services.exchange_filter import ExchangeFilter


class TradeSenseService:
    def __init__(self):
        bitcoin_dto = BitcoinDTO()
        self.cmc_service = CoinMarketCapService(bitcoin_dto)
        self.arbitrage_service = ArbitrageService()
        self.exchange_filter = ExchangeFilter()

    def start_trading(self):
        market_pairs = self.cmc_service.get_market_pairs()
        filtered_market_pairs, length = self.exchange_filter.filter_exchanges(market_pairs)
        self.arbitrage_service.calculate_arbitrage(filtered_market_pairs, length)



if __name__ == '__main__':
    ob = TradeSenseService()
    ob.start_trading()
