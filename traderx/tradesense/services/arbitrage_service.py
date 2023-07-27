"""
Arbitrage service
"""


class ArbitrageService:
    def __int__(self):
        pass

    def calculate_arbitrage(self, filtered_market_pairs, length):
        #print(filtered_market_pairs)
        arbitrage_amt = filtered_market_pairs[0]["quotes"][0]["price"] - filtered_market_pairs[length-1]["quotes"][0]["price"]
        print(arbitrage_amt)