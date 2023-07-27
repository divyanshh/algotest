from django.contrib import admin

from tradesense.models.crypto import Cryptos
from tradesense.models.trades import Trades
from tradesense.models.exchange import Exchange


# Register your models here.

class CryptoAdmin(admin.ModelAdmin):
    list_display = ["id", "slug", "crypto_name", "symbol", "quote_currency_id", "sort", "sort_direction",
                    "limit", "start", "category", "market_pair"]


class ExchangeAdmin(admin.ModelAdmin):
    list_display = ["id", "exchange_name", "slug", "is_active"]


class TradesAdmin(admin.ModelAdmin):
    list_display = ["id", "crypto_name", "slug", "quote_currency_id", "market_pair",
                    "buy_exchange", "sell_exchange", "buy_price", "sell_price",
                    "arbitrage"]


admin.site.register(Cryptos, CryptoAdmin)
admin.site.register(Trades, TradesAdmin)
admin.site.register(Exchange, ExchangeAdmin)
