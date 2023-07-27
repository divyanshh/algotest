from django.db import models


class Cryptos(models.Model):
    """
    Cryptos Model
    """

    id = models.AutoField(primary_key=True)
    crypto_name = models.CharField(max_length=300, unique=True)
    slug = models.CharField(max_length=300, unique=True)
    quote_currency_id = models.IntegerField(default=0)
    sort = models.CharField(max_length=300)
    sort_direction = models.CharField(
        max_length=30,
        default="desc",
        choices=[("ASC", "asc"), ("DESC", "desc")],
    )
    limit = models.IntegerField(default=100)
    start = models.IntegerField(default=1)
    category = models.CharField(max_length=300)
    market_pair = models.CharField(max_length=30)
