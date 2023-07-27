from tradesense.dto.crypto_dtos.crypto_dto import CryptoDTO


class TetherDTO(CryptoDTO):  # USDT
    def __init__(self):
        super().__init__(slug="tether")
