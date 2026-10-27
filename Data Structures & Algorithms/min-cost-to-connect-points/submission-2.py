import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if not n:
            return 0
        # cost, point
        heap = [(0, 0)] # cost, index
        visited = set()
        result = 0

        def get_distance(p1, p2):
            x1, y1 = p1
            x2, y2 = p2

            return abs(x1 - x2) + abs(y1 - y2)

        while heap:
            cost, index = heapq.heappop(heap)

            if index in visited:
                continue
            
            visited.add(index)
            result += cost
            p1 = points[index]

            for j in range(n):
                if j in visited:
                    continue

                p2 = points[j]
                
                dist = get_distance(p1, p2)

                heapq.heappush(heap, (dist, j))

        return result
        