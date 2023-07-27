from tradesense.dto.arbitrage_dto import ArbitrageDTO

from tradesense.models.trades import Trades


class TradesRepository:

    @staticmethod
    def add_entry(arbitrage_dto: ArbitrageDTO) -> None:
        crypto_id = arbitrage_dto
        trade = Trades()
