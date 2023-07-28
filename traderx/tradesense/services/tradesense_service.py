"""
TradeSenseService
"""
from tradesense.services.arbitrage_service import ArbitrageService
from tradesense.services.coinmarketcap_service import CoinMarketCapService
from tradesense.services.exchange_filter_service import ExchangeFilterService

from tradesense.dto.arbitrage_dto import ArbitrageDTO

from tradesense.repository.trades_repository import TradesRepository

from tradesense.repository.crypto_repository import CryptoRepository


class TradeSenseService:
    """
    TradeSenseService is the core service of this application
    The core functionality if this service is to use all the
    other services to enable trading
    """

    def __init__(self, crypto_id: int):
        self.crypto_model = CryptoRepository().get_crypto_details(crypto_id)
        self.cmc_service = CoinMarketCapService(self.crypto_model)
        self.arbitrage_service = ArbitrageService()
        self.exchange_filter_service = ExchangeFilterService()
        self.trades_repository = TradesRepository()

    def start_trading(self) -> ArbitrageDTO:
        """
        Enable trading
        Load crypto model, get market data for different exchanges
        and filter according to active exchanges for the user.
        Additionally add entry to trades model for analytics

        :return: ArbitrageDTO
        """
        arbitrage_dto = ArbitrageDTO()
        arbitrage_dto.crypto = self.crypto_model
        market_pairs = self.cmc_service.get_market_pairs()
        filtered_market_pairs, length = self.exchange_filter_service.filter_exchanges(
            market_pairs, self.crypto_model.market_pair
        )
        arbitrage_dto = self.arbitrage_service.calculate_arbitrage(
            arbitrage_dto, filtered_market_pairs, length
        )
        self.trades_repository.add_entry(
            arbitrage_dto
        )  # This would ideally be done via CDCs or background jobs
        return arbitrage_dto
