import collections, heapq



class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)

        for src, dst, weight in times:
            adj[src].append((dst, weight))

        heap = [(0, k)]
        visited  = set()
        max_time = 0

        while heap:
            time, node = heapq.heappop(heap)

            if node in visited:
                continue

            visited.add(node)
            max_time = max(max_time, time)

            for neighbor, weight in adj[node]:
                if neighbor not in visited:
                    heapq.heappush(heap, (time + weight, neighbor))

        return max_time if len(visited) == n else -1

