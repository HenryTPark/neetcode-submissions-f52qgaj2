class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # O(N) Time | O(1) Space
        result = 0
        min_buy_price = float('inf')

        for price in prices:
            min_buy_price = min(price, min_buy_price)

            result = max(result, price - min_buy_price)

        return result
        