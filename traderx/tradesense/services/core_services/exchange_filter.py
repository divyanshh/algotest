class ExchangeFilter:
    def __init__(self, market_pair="BTC/USD"):
        self.exchanges = {"binance": True, "coinbase": True, "kraken": True, "bitfinex": True, "bittrex": True}
        self.market_pair = market_pair

    def filter_exchanges(self, market_pairs):
        filtered_market_pairs = []
        length = 0
        for market_pair in market_pairs:
            if market_pair["exchangeSlug"] in self.exchanges and market_pair["marketPair"] == self.market_pair:
                filtered_market_pairs.append(market_pair)
                length += 1
        return filtered_market_pairs, length
