import threading

from django.http import HttpResponse
from django.shortcuts import render

from tradesense.services.core_services.tradesense_service import TradeSenseService


# Create your views here.

def start_trading(request):
    tradesense_service = TradeSenseService()
    threading.Timer(5.0, tradesense_service.start_trading()).start()
    return HttpResponse("Hello, world. You're at the stocks signals.")
