from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(key=lambda x: x[1], reverse=True)
        itinerary = []

        adj_list = defaultdict(list)

        for src, dest in tickets:
            adj_list[src].append(dest)

        def build_itinerary(airport):
            while adj_list[airport]:
                next_airport = adj_list[airport].pop()
                build_itinerary(next_airport)

            itinerary.append(airport)

        build_itinerary('JFK')
        return itinerary[::-1]
        