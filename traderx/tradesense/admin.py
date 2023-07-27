from django.contrib import admin

from tradesense.models.crypto import Cryptos
from tradesense.models.trades import Trades


# Register your models here.

class CryptoAdmin(admin.ModelAdmin):
    list_display = ["id", "slug", "quote_currency_id", "sort", "sort_direction",
                    "limit", "start", "category", "market_pair"]


admin.site.register(Cryptos, CryptoAdmin)
