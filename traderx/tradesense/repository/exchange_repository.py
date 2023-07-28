from tradesense.models.exchange import Exchange


class ExchangeRepository:
    """
    DB layer to save and get Exchange details from DB
    """

    @staticmethod
    def get_exchange_details(slug):
        return Exchange.objects.filter(slug=slug)[0]
