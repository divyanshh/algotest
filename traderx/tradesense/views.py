import threading
import time

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from tradesense.repository.crypto_repository import CryptoRepository
from tradesense.services.analytics_service import AnalyticsService
from tradesense.services.socket_service import SocketService
from tradesense.services.tradesense_service import TradeSenseService
from tradesense.utils import get_message


# Create your views here.
@api_view(["GET"])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def start_trading(request):
    crypto_id = int(request.GET["id"])
    if crypto_id is None:
        raise ValueError("Please pass crypto's id to trade in")
    conn = SocketService.get_connection()

    # Start a separate thread to handle threshold setting
    threshold_thread = threading.Thread(target=handle_threshold, args=(conn, crypto_id))
    threshold_thread.start()

    while True:
        tradesense_service = TradeSenseService(crypto_id)
        arbitrage_dto = tradesense_service.start_trading()
        msg = get_message(arbitrage_dto)
        print(msg)
        conn.send(str(msg).encode())  # send data to the client
        time.sleep(60)


def handle_threshold(conn, crypto_id):
    while True:
        data = conn.recv(1024).decode()
        if data:
            # set_threshold:400
            try:
                threshold = int(data.split(":")[1])
                CryptoRepository.update_crypto_threshold(crypto_id, threshold)
                conn.send("Threshold successfully updated!".encode())
            except Exception as ex:
                conn.send(str(ex).encode())


@api_view(["GET"])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def analytics_view(request):
    analytics_dto = AnalyticsService().get_trade_analytics(request.GET)
    return Response(analytics_dto.to_json())
