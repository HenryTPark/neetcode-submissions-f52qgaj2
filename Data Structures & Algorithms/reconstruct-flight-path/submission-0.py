from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        # O(ELog(E)) Time | O(V + E) Space
        tickets.sort(key=lambda x: x[1], reverse=True)

        adj_list = defaultdict(list)

        for src, dst in tickets:
            adj_list[src].append(dst)

        itinerary = []

        def build_itinerary(airport):
            while adj_list[airport]:
                next_airport = adj_list[airport].pop()
                build_itinerary(next_airport)

            itinerary.append(airport)

        build_itinerary("JFK")

        return itinerary[::-1]
