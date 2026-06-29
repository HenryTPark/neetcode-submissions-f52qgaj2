class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # O(N) Time | O(1) Space
        min_buy_price = float('inf')
        max_profit = 0

        for price in prices:
            min_buy_price = min(min_buy_price, price)
            profit = price - min_buy_price

            max_profit = max(max_profit, profit)


        return max_profit
        



        
        