from tradesense.models.crypto import Crypto


class ArbitrageDTO:
    buy_exchange = str
    sell_exchange = str
    buy_price = float
    sell_price = float
    arbitrage = float
    min_arbitrage = float
    success = bool
    crypto = Crypto
