from tradesense.dto.arbitrage_dto import ArbitrageDTO
from tradesense.models.exchange import Exchange

from tradesense.models.trades import Trades


class TradesRepository:
    """
    DB layer to save and get Trade details from DB
    """

    @staticmethod
    def add_entry(arbitrage_dto: ArbitrageDTO) -> None:
        crypto = arbitrage_dto.crypto
        min_arbitrage = (
            arbitrage_dto.min_arbitrage
        ) = arbitrage_dto.crypto.arbitrage_threshold_amount
        buy_exchange = Exchange.objects.filter(slug=arbitrage_dto.buy_exchange)[0]
        sell_exchange = Exchange.objects.filter(slug=arbitrage_dto.sell_exchange)[0]
        arbitrage_dto.success = success = (
            True if arbitrage_dto.arbitrage >= min_arbitrage else False
        )
        trade = Trades(
            crypto=crypto,
            buy_exchange=buy_exchange,
            sell_exchange=sell_exchange,
            quote_currency_id=arbitrage_dto.crypto.quote_currency_id,
            buy_price=arbitrage_dto.buy_price,
            sell_price=arbitrage_dto.sell_price,
            arbitrage=round(arbitrage_dto.arbitrage, 3),
            market_pair=arbitrage_dto.crypto.market_pair,
            success=success,
            min_arbitrage=min_arbitrage,
        )
        trade.save()
