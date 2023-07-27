from tradesense.dto.arbitrage_dto import ArbitrageDTO
from tradesense.models.exchange import Exchange
from tradesense.models.min_arbitrage import ArbitrageThreshold

from tradesense.models.trades import Trades


class TradesRepository:

    @staticmethod
    def add_entry(arbitrage_dto: ArbitrageDTO) -> None:
        crypto_id = arbitrage_dto.crypto.id
        min_arbitrage = arbitrage_dto.min_arbitrage = ArbitrageThreshold.objects.filter(id=1).arbitrage_threshold_amount
        buy_exchange_id = Exchange.objects.filter(slug=arbitrage_dto.buy_exchange).id
        sell_exchange_id = Exchange.objects.filter(slug=arbitrage_dto.sell_exchange).id
        arbitrage_dto.success = success = True if arbitrage_dto.arbitrage >= min_arbitrage else False
        trade = Trades(crypto=crypto_id, buy_exchange=buy_exchange_id, sell_exchange=sell_exchange_id,
                       quote_currency_id=arbitrage_dto.crypto.quote_currency_id, buy_price=arbitrage_dto.buy_price,
                       sell_price=arbitrage_dto.sell_price, arbitrage=arbitrage_dto.arbitrage,
                       market_pair=arbitrage_dto.crypto.market_pair, success=success, min_arbitrage=min_arbitrage)
        trade.save()
