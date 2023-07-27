from django.db import models


class Trades(models.Model):
    """
    Trades model
    """

    id = models.AutoField(primary_key=True)
    crypto_id = models.ForeignKey("Crypto", on_delete=models.CASCADE)
    quote_currency_id = models.IntegerField(default=2781)
    buy_exchange_id = models.ForeignKey("Exchange", on_delete=models.CASCADE)
    sell_exchange_id = models.ForeignKey("Exchange", on_delete=models.CASCADE)
    buy_price = models.FloatField(default=0)
    sell_price = models.FloatField(default=0)
    arbitrage = models.FloatField(default=0)
