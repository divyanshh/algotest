from django.core.exceptions import ValidationError
from django.db import models


class Crypto(models.Model):
    """
    Crypto Model
    """

    id = models.AutoField(primary_key=True)
    crypto_name = models.CharField(max_length=300, unique=True)
    symbol = models.CharField(max_length=30, unique=True, default="")
    slug = models.CharField(max_length=300, unique=True)
    quote_currency_id = models.IntegerField(default=2781)  # 2781 is default for USD
    sort = models.CharField(max_length=300, default="price")
    sort_direction = models.CharField(
        max_length=30,
        default="desc",
        choices=[("asc", "asc"), ("desc", "desc")],
    )
    limit = models.IntegerField(default=100)
    start = models.IntegerField(default=1)
    category = models.CharField(max_length=300, default="spot")
    market_pair = models.CharField(max_length=30)

    def clean(self):
        if any(ele.isupper() for ele in str(self.slug)):
            raise ValidationError("Slug cannot contain uppercase values.")
        if any(ele.islower() for ele in str(self.symbol)):
            raise ValidationError("Symbol cannot contain lowercase values.")
