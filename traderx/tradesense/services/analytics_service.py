from django.db.models import Avg

from tradesense.dto.analytics_dto import AnalyticsDTO
from tradesense.models.trades import Trades


class AnalyticsService:
    """
    Analytics service - Handles all analytics requests
    """

    @staticmethod
    def get_trade_analytics(get_request) -> AnalyticsDTO:
        """
        get details from GET request
        Filter based on from_date, to_date, success, crypto_id
        from_exchange, to_exchange, min_arbitrage and return a
        collation of results + all the trades that took place

        :param get_request:
        :return: AnalyticsDTO
        """
        if "from_date" not in get_request:
            raise ValueError("Required from_date")
        if "to_date" not in get_request:
            raise ValueError("Required to_date")
        from_date = get_request["from_date"]
        to_date = get_request["to_date"]
        successful = None
        results = None

        if "successful" in get_request:
            successful = True if get_request["successful"] == "True" else False
        if successful is None:
            results = Trades.objects.filter(created_at__range=(from_date, to_date))
        else:
            results = Trades.objects.filter(
                created_at__range=(from_date, to_date), success=successful
            )

        if "crypto_id" in get_request:
            ids = get_request["crypto_id"].split(",")
            results = results.filter(crypto__in=ids)
        if "from_exchange" in get_request:
            ids = get_request["from_exchange"].split(",")
            results = results.filter(buy_exchange__in=ids)
        if "to_exchange" in get_request:
            ids = get_request["to_exchange"].split(",")
            results = results.filter(sell_exchange__in=ids)
        if "min_arbitrage" in get_request:
            min_arbitrage = int(get_request["min_arbitrage"])
            results = results.filter(arbitrage__gte=min_arbitrage)
        if len(results) == 0:
            return AnalyticsDTO(from_date, to_date)
        average_profit = (
            0
            if successful is False
            else round(
                results.filter(success=True)
                .values_list("success")
                .annotate(Avg("arbitrage"))[0][1],
                2,
            )
        )
        analytics_dto = AnalyticsDTO(
            number_of_trades=len(results),
            successful_trades=len(results.filter(success=True)),
            failed_trades=len(results.filter(success=False)),
            average_profit=average_profit,
            trades=results.all(),
            from_date=from_date,
            to_date=to_date,
        )
        return analytics_dto
