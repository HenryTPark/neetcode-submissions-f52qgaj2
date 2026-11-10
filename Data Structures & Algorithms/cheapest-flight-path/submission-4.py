class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for _ in range(k + 1):
            temp_prices = prices.copy()

            for source, dest, cost in flights:
                if prices[source] == float("inf"):
                    continue

                if prices[source] + cost < temp_prices[dest]:
                    temp_prices[dest] = prices[source] + cost

            prices = temp_prices

        return prices[dst] if prices[dst] < float("inf") else -1
