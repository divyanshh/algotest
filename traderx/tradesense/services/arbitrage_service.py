"""
Arbitrage service
"""


class ArbitrageService:
    @staticmethod
    def calculate_arbitrage(filtered_market_pairs, length):
        arbitrage_amt = filtered_market_pairs[0]["quotes"][0]["price"] \
                        - filtered_market_pairs[length - 1]["quotes"][0]["price"]
        print(arbitrage_amt)
