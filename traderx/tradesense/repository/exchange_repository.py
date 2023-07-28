from tradesense.models.exchange import Exchange


class ExchangeRepository:
    @staticmethod
    def get_exchange_details(slug):
        return Exchange.objects.filter(slug=slug)[0]
