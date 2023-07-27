"""
TradeSenseService
"""
from traderx.tradesense.services.arbitrage_service import ArbitrageService
from traderx.tradesense.services.coinmarketcap_service import CoinMarketCapService
from traderx.tradesense.services.crypto_dtos.bitcoin_dto import BitcoinDTO


class TradeSenseService:
    def __init__(self):
        bitcoin_dto = BitcoinDTO()
        self.cmc_service = CoinMarketCapService(bitcoin_dto)
        self.arbitrage_service = ArbitrageService()

    def start_trading(self):
        market_pairs = self.cmc_service.get_market_pairs()
        print(market_pairs)


if __name__ == '__main__':
    ob = TradeSenseService()
    ob.start_trading()