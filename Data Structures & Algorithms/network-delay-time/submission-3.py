import collections, heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)

        for s, d, w in times:
            adj[s].append((d, w))

        heap = [(0, k)]
        max_time = 0
        visited = set()

        while heap:
            time, node = heapq.heappop(heap)

            if node in visited:
                continue

            max_time = max(max_time, time)
            visited.add(node)

            for d, w in adj[node]:
                if d not in visited:
                    heapq.heappush(heap, (w + time, d))

        return max_time if len(visited) == n else -1        