class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        # O(E * K) Time | O(V) Space
        # E: number of flights (edges) | K: maximum stops allowed | V: number of cities (nodes)

        """
        Uses a variation of the Bellman-Ford algorithm.
        Limits the edge relaxations to k + 1 iterations to satisfy the stops constraint.
        """
        prices = [float("inf")] * n
        prices[src] = 0

        # We can take at most k + 1 edges (flights)
        for _ in range(k + 1):
            # Create a temporary array to ensure we only use prices from the previous iteration/stop
            tmp_prices = prices.copy()

            for source, dest, cost in flights:
                if prices[source] == float("inf"):
                    continue

                if prices[source] + cost < tmp_prices[dest]:
                    tmp_prices[dest] = prices[source] + cost

            prices = tmp_prices

        return prices[dst] if prices[dst] != float("inf") else -1