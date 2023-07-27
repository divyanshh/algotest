import logging
import socket
import threading
import time

from django.http import HttpResponse
from django.shortcuts import render

from tradesense.services.core_services.tradesense_service import TradeSenseService
from tradesense.services.core_services.socket_service import SocketService


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
