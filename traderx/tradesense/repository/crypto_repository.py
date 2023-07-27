from tradesense.models.crypto import Crypto


class CryptoRepository:

    @staticmethod
    def get_crypto_details(crypto_id):
        return Crypto.objects.filter(id=crypto_id)
