from django.urls import path

from . import views

urlpatterns = [
    path("start_trading", views.start_trading, name="start_trading"),
]
