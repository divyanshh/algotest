from tradesense.models.crypto import Crypto


class ArbitrageDTO:
    """
    Contains all the data for a trade that takes place in the application
    """

    buy_exchange = str
    sell_exchange = str
    buy_price = float
    sell_price = float
    arbitrage = float
    min_arbitrage = float
    success = bool
    crypto = Crypto
