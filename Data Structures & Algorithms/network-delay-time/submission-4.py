from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        
        for source, target, weight in times:
            adj[source].append((weight, target))

        heap = [(0, k)]
        max_time = 0
        visited = set()

        while heap:
            time, node = heapq.heappop(heap)

            if node in visited:
                continue

            visited.add(node)
            max_time = max(max_time, time)

            for weight, neighbor in adj[node]:
                if neighbor not in visited:
                    heapq.heappush(heap, (weight + time, neighbor))

        return max_time if len(visited) == n else -1

        

        
        