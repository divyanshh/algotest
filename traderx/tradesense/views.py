import time

from tradesense.services.tradesense_service import TradeSenseService
from tradesense.services.socket_service import SocketService


# Create your views here.

def start_trading(request):
    tradesense_service = TradeSenseService()
    conn = SocketService.get_connection()
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        # data = conn.recv(1024).decode()
        # # print("from connected user: " + str(data))
        # if data == "break":
        #     break
        arbitrage_amt = tradesense_service.start_trading()
        # data = input(' -> ')
        conn.send(str(arbitrage_amt).encode())  # send data to the client
        time.sleep(5)
    #conn.close()  # close the connection
