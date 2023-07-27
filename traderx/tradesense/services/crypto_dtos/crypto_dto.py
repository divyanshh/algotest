from abc import ABC


class CryptoDTO(ABC):
    """
    Abstract DTO for all cryptos
    """
    def __init__(self, slug: str, quote_currency_id="2781", sort="price", sort_direction="desc", limit="100", start="1",
                 category="all"):
        self.slug = slug
        self.quote_currency_id = quote_currency_id
        self.sort = sort
        self.sort_direction = sort_direction
        self.limit = limit
        self.start = start
        self.category = category
