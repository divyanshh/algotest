from tradesense.models.exchange import Exchange


class ExchangeFilter:

    @staticmethod
    def filter_exchanges(market_pairs, crypto_vs_curr_pair):
        exchanges_qs = Exchange.objects.filter(is_active=True).values('slug', 'is_active')
        exchanges = {item['slug']: item['is_active'] for item in list(exchanges_qs)}
        filtered_market_pairs = []
        length = 0
        for market_pair in market_pairs:
            if market_pair["exchangeSlug"] in exchanges and market_pair["marketPair"] == crypto_vs_curr_pair:
                filtered_market_pairs.append(market_pair)
                length += 1
        return filtered_market_pairs, length
