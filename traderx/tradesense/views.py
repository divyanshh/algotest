import time

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from tradesense.services.analytics_service import AnalyticsService
from tradesense.services.tradesense_service import TradeSenseService


# Create your views here.
@api_view(["GET"])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def start_trading(request):
    crypto_id = int(request.GET["id"])
    if crypto_id is None:
        raise ValueError("Please pass crypto's id to trade in")
    tradesense_service = TradeSenseService(crypto_id)
    # conn = SocketService.get_connection()
    while True:
        arbitrage_dto = tradesense_service.start_trading()
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
        print(msg1 + msg2)
        # conn.send(str(msg1+msg2).encode())  # send data to the client
        tradesense_service = TradeSenseService(crypto_id)
        time.sleep(10)


@api_view(["GET"])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def analytics_view(request):
    analytics_dto = AnalyticsService().get_trade_analytics(request.GET)
    return Response(analytics_dto.to_json())
