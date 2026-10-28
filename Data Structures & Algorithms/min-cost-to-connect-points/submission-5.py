class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # O(N^2) Time | O(N) Space
        n = len(points)
        min_dist = [float('inf')] * n
        min_dist[0] = 0
        result = 0
        visited = set()

        for _ in range(n):
            node = -1
            curr_min = float('inf')

            for i in range(n):
                if i not in visited and min_dist[i] < curr_min:
                    node = i
                    curr_min = min_dist[i]

            result += curr_min
            visited.add(node)

            for next_node in range(n):
                if next_node not in visited:
                    dist = abs(points[node][0] - points[next_node][0]) + abs(points[node][1] - points[next_node][1])

                    if dist < min_dist[next_node]:
                        min_dist[next_node] = dist

        return result
        