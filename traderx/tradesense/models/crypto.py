from django.core.exceptions import ValidationError
from django.db import models


class Crypto(models.Model):
    """
    Crypto Model
    Stores all the data for a crypto

    CMC means CoinMarketCap in the below comments
    """

    id = models.AutoField(primary_key=True)
    crypto_name = models.CharField(max_length=300, unique=True)
    symbol = models.CharField(max_length=30, unique=True, default="")  # eg BTC
    slug = models.CharField(
        max_length=300, unique=True
    )  # unique key for CMC, eg - bitcoin
    quote_currency_id = models.IntegerField(
        default=2781
    )  # 2781 is default for USD, currency you trade in
    sort = models.CharField(
        max_length=300, default="price"
    )  # sort CMC exchanges data acc to this field
    sort_direction = models.CharField(  # sort in ascending or descending order
        max_length=30,
        default="desc",
        choices=[("asc", "asc"), ("desc", "desc")],
    )
    limit = models.IntegerField(default=100)  # limit of results
    start = models.IntegerField(default=1)  # for pagination
    category = models.CharField(max_length=300, default="spot")
    market_pair = models.CharField(max_length=30)  # eg BTC/USD
    arbitrage_threshold_amount = models.FloatField(
        default=0
    )  # Our threshold to take trades for this crypto
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if any(ele.isupper() for ele in str(self.slug)):
            raise ValidationError("Slug cannot contain uppercase values.")
        if any(ele.islower() for ele in str(self.symbol)):
            raise ValidationError("Symbol cannot contain lowercase values.")
