from tradesense.dto.arbitrage_dto import ArbitrageDTO


def get_message(arbitrage_dto: ArbitrageDTO) -> str:
    msg1 = "TRADE SUCCESS : " if arbitrage_dto.success else "TRADE FAILURE : "
    msg2 = (
        "Crypto: {crypto}, From: {from_exchange} To: {to_exchange}, buy_price: {buy_price} , "
        "sell_price: {sell_price} arbitrage_amt: {arbitrage_amt}, "
        "min_arbitrage: {min_arbitrage}".format(
            crypto=arbitrage_dto.crypto.crypto_name,
            from_exchange=arbitrage_dto.buy_exchange,
            to_exchange=arbitrage_dto.sell_exchange,
            buy_price=arbitrage_dto.buy_price,
            sell_price=arbitrage_dto.sell_price,
            arbitrage_amt=arbitrage_dto.arbitrage,
            min_arbitrage=arbitrage_dto.min_arbitrage,
        )
    )
    return msg1 + msg2
