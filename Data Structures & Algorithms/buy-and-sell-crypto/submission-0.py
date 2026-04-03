class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # O(N) Time | O(1) Space
        # N: number of elements
        res = 0
        min_buy_price = float('inf')

        for price in prices:
            min_buy_price = min(min_buy_price, price)

            profit = price - min_buy_price
            res = max(profit, res)

        return res
        