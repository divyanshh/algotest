"""
TradeSenseService
"""
from tradesense.services.arbitrage_service import ArbitrageService
from tradesense.services.coinmarketcap_service import CoinMarketCapService
from tradesense.services.exchange_filter import ExchangeFilter

from tradesense.dto.arbitrage_dto import ArbitrageDTO

from tradesense.repository.trades_repository import TradesRepository

from tradesense.repository.crypto_repository import CryptoRepository


class TradeSenseService:
    def __init__(self, crypto_id: int):
        self.crypto_model = CryptoRepository().get_crypto_details(crypto_id)
        self.cmc_service = CoinMarketCapService(self.crypto_model)
        self.arbitrage_service = ArbitrageService()
        self.exchange_filter = ExchangeFilter()
        self.trades_repository = TradesRepository()

    def start_trading(self) -> ArbitrageDTO:
        arbitrage_dto = ArbitrageDTO()
        arbitrage_dto.crypto = self.crypto_model
        market_pairs = self.cmc_service.get_market_pairs()
        filtered_market_pairs, length = self.exchange_filter.filter_exchanges(market_pairs,
                                                                              self.crypto_model.market_pair)
        arbitrage_dto = self.arbitrage_service.calculate_arbitrage(arbitrage_dto, filtered_market_pairs, length)
        self.trades_repository.add_entry(arbitrage_dto)
        return arbitrage_dto
