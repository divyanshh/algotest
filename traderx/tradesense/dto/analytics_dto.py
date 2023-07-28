from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder


class AnalyticsDTO:

    def __init__(self, from_date, to_date, number_of_trades=0, successful_trades=0, failed_trades=0,
                 average_profit=0, trades=None):
        if trades is None:
            trades = []
        self.number_of_trades = number_of_trades
        self.successful_trades = successful_trades
        self.failed_trades = failed_trades
        self.average_profit = average_profit
        self.from_date = from_date
        self.to_date = to_date
        self.trades = trades

    def to_json(self):
        # Serialize the trades queryset to JSON
        # trades_json = serializers.serialize('json', self.trades, cls=DjangoJSONEncoder)
        trades_json = serializers.serialize('python', self.trades)

        json_data = {
            "number_of_trades": self.number_of_trades,
            "successful_trades": self.successful_trades,
            "failed_trades": self.failed_trades,
            "average_profit": self.average_profit,
            "from_date": self.from_date,
            "to_date": self.to_date,
            "trades": trades_json,
        }
        print(json_data)
        return json_data
