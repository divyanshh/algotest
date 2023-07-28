from django.db import models


class Trades(models.Model):
    """
    Trades model - For maintaining analytics
    """

    id = models.AutoField(primary_key=True)
    crypto = models.ForeignKey("Crypto", on_delete=models.CASCADE)
    quote_currency_id = models.IntegerField(
        default=2781
    )  # In which currency the trade took place
    buy_exchange = models.ForeignKey(  # The exchange the crypto was bought from
        "Exchange", on_delete=models.CASCADE, related_name="buy_exchange_id"
    )
    sell_exchange = models.ForeignKey(  # The exchange the crypto was sold to
        "Exchange", on_delete=models.CASCADE, related_name="sell_exchange_id"
    )
    buy_price = models.FloatField(default=0)
    sell_price = models.FloatField(default=0)
    arbitrage = models.FloatField(default=0)  # How much did we earn
    market_pair = models.CharField(max_length=30)  # eg - BTC/USD
    min_arbitrage = models.FloatField(
        default=0
    )  # What was the min arbitrage threshold during this trade
    success = models.BooleanField(
        default=False
    )  # If the trade was a success or a failure based on threshold
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    last_updated_at = models.DateTimeField(auto_now=True)
