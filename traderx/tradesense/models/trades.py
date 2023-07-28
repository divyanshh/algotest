from django.db import models


class Trades(models.Model):
    """
    Trades model
    """

    id = models.AutoField(primary_key=True)
    crypto = models.ForeignKey("Crypto", on_delete=models.CASCADE)
    quote_currency_id = models.IntegerField(default=2781)
    buy_exchange = models.ForeignKey(
        "Exchange", on_delete=models.CASCADE, related_name="buy_exchange_id"
    )
    sell_exchange = models.ForeignKey(
        "Exchange", on_delete=models.CASCADE, related_name="sell_exchange_id"
    )
    buy_price = models.FloatField(default=0)
    sell_price = models.FloatField(default=0)
    arbitrage = models.FloatField(default=0)
    market_pair = models.CharField(max_length=30)
    min_arbitrage = models.FloatField(default=0)
    success = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    last_updated_at = models.DateTimeField(auto_now=True)
