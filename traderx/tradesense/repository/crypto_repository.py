from tradesense.models.crypto import Crypto


class CryptoRepository:
    @staticmethod
    def get_crypto_details(crypto_id):
        return Crypto.objects.filter(id=crypto_id)[0]

    @staticmethod
    def update_crypto_threshold(id, threshold):
        crypto = Crypto.objects.filter(id=id)[0]
        crypto.arbitrage_threshold_amount = threshold
        crypto.save()
