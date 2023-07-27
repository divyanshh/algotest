from traderx.tradesense.services.crypto_dtos.crypto_dto import CryptoDTO


class EthereumDTO(CryptoDTO):
    def __init__(self):
        super().__init__(slug="ethereum")
