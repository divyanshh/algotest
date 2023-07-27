from django.core.exceptions import ValidationError
from django.db import models


class ArbitrageThreshold(models.Model):
    """
    MinArbitrage Model
    """

    id = models.AutoField(primary_key=True)
    arbitrage_threshold_amount = models.FloatField(default=0)
