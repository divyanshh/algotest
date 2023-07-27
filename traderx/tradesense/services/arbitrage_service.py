"""
Arbitrage service
"""
import logging

from tradesense.dto.arbitrage_dto import ArbitrageDTO


class ArbitrageService:

    @staticmethod
    def calculate_arbitrage(filtered_market_pairs, length: int) -> ArbitrageDTO:
        """
        Calculates arbitrage b/w the first and last Exchanges
        (assuming exchanges data is sorted in descending order by price)

        :param filtered_market_pairs:
        :param length:
        :return: ArbitrageDTO
        """

        quotes = "quotes"
        price = "price"
        exchange_slug = "exchangeSlug"
        arbitrage_amt = -1

        try:
            arbitrage_amt = filtered_market_pairs[0][quotes][0][price] \
                            - filtered_market_pairs[length - 1][quotes][0][price]
        except Exception as ex:
            logging.error(str(ex))
            raise RuntimeError("Arbitrage couldn't be calculated")
        arbitrage_dto = ArbitrageDTO()
        arbitrage_dto.arbitrage = arbitrage_amt
        arbitrage_dto.buy_price = filtered_market_pairs[length - 1][quotes][0][price]
        arbitrage_dto.sell_price = filtered_market_pairs[0][quotes][0][price]
        arbitrage_dto.from_exchange = filtered_market_pairs[length - 1][exchange_slug]
        arbitrage_dto.to_exchange = filtered_market_pairs[0][exchange_slug]
        return arbitrage_dto
