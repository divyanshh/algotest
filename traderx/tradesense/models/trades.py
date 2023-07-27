from django.db import models


class Trades(models.Model):
    """
    Trades Model
    """

    id = models.AutoField(primary_key=True)
    crypto_name = models.CharField(max_length=300, unique=True)
    slug = models.CharField(max_length=300, unique=True)
    quote_currency_id = models.IntegerField(default=0)
    market_pair = models.CharField(max_length=30)
    buy_exchange = models.CharField(max_length=30)
    sell_exchange = models.CharField(max_length=30)
    buy_price = models.FloatField(default=0)
    sell_price = models.FloatField(default=0)
    arbitrage = models.FloatField(default=0)
