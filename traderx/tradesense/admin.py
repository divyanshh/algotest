from django.contrib import admin

from tradesense.models.crypto import Crypto
from tradesense.models.trades import Trades
from tradesense.models.exchange import Exchange


# Register your models here.

class CryptoAdmin(admin.ModelAdmin):
    list_display = ["id", "slug", "crypto_name", "symbol", "quote_currency_id", "sort", "sort_direction",
                    "limit", "start", "category", "market_pair", "arbitrage_threshold_amount"]


class ExchangeAdmin(admin.ModelAdmin):
    list_display = ["id", "exchange_name", "slug", "is_active"]


class TradesAdmin(admin.ModelAdmin):
    list_display = ["id", "crypto_id", "quote_currency_id",
                    "buy_exchange_id", "sell_exchange_id", "buy_price", "sell_price",
                    "arbitrage", "min_arbitrage", "success", "created_at"]


admin.site.register(Crypto, CryptoAdmin)
admin.site.register(Trades, TradesAdmin)
admin.site.register(Exchange, ExchangeAdmin)
