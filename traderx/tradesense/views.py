import time

from tradesense.services.tradesense_service import TradeSenseService
from tradesense.services.socket_service import SocketService


# Create your views here.

def start_trading(request):
    crypto_id = int(request.GET['id'])
    if crypto_id is None:
        raise ValueError("Please pass crypto's id to trade in")
    tradesense_service = TradeSenseService(crypto_id)
    conn = SocketService.get_connection()
    while True:
        arbitrage_dto = tradesense_service.start_trading()
        msg1 = "TRADE SUCCESS : " if arbitrage_dto.success else "TRADE FAILURE : "
        msg2 = "From: {from_exchange} To: {to_exchange}, buy_price: {buy_price} , sell_price: {sell_price} " \
               "arbitrage_amt: {arbitrage_amt}," \
               " min_arbitrage: {min_arbitrage}".format(from_exchange=arbitrage_dto.buy_exchange,
                                                        to_exchange=arbitrage_dto.sell_exchange,
                                                        buy_price=arbitrage_dto.buy_price,
                                                        sell_price=arbitrage_dto.sell_price,
                                                        arbitrage_amt=arbitrage_dto.arbitrage,
                                                        min_arbitrage=arbitrage_dto.min_arbitrage)
        conn.send(str(msg1+msg2).encode())  # send data to the client
        time.sleep(10)
