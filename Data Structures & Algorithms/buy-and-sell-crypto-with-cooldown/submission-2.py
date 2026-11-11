class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        held = -float("inf")  # holding on to the stock
        sold = 0  # selling today
        rest = 0  # everything else

        for price in prices:
            prev_held = held
            held = max(held, rest - price)
            rest = max(rest, sold)

            sold = prev_held + price

        return max(sold, rest)
