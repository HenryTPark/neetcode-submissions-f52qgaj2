import collections, heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for source, target, time in times:
            adj[source].append((target, time))

        heap = [(0, k)]
        visited = set()
        max_time = 0

        while heap:
            time, node = heapq.heappop(heap)

            if node in visited:
                continue

            visited.add(node)
            max_time = max(max_time, time)

            for dst, tim in adj[node]:
                if dst not in visited:
                    heapq.heappush(heap, (tim + time, dst))

        return max_time if len(visited) == n else -1




        