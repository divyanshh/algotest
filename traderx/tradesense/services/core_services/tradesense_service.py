"""
TradeSenseService
"""
from tradesense.services.core_services.arbitrage_service import ArbitrageService
from tradesense.services.core_services.coinmarketcap_service import CoinMarketCapService
from tradesense.dto.crypto_dtos.bitcoin_dto import BitcoinDTO
from tradesense.services.core_services.exchange_filter import ExchangeFilter


class TradeSenseService:
    def __init__(self):
        crypto_dto = BitcoinDTO()
        # crypto_dto = EthereumDTO()
        self.cmc_service = CoinMarketCapService(crypto_dto)
        self.arbitrage_service = ArbitrageService()
        self.exchange_filter = ExchangeFilter()
        # self.exchange_filter = ExchangeFilter("ETH/USD")

    def start_trading(self):
        market_pairs = self.cmc_service.get_market_pairs()
        filtered_market_pairs, length = self.exchange_filter.filter_exchanges(market_pairs)
        self.arbitrage_service.calculate_arbitrage(filtered_market_pairs, length)



if __name__ == '__main__':
    ob = TradeSenseService()
    ob.start_trading()
