class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # O(E log V) Time | O(E + V) Space
        # E: number of edges (len of times) | V: number of vertices (n)

        """
        Uses Dijkstra's algorithm to find the shortest time to reach every node.
        Returns the maximum time found, or -1 if not all nodes are reachable.
        """
        # Build adjacency list representation of the graph
        adj = collections.defaultdict(list)
        for src, dst, weight in times:
            adj[src].append((dst, weight))

        # Min-heap stores tuples of (accumulated_time, node)
        heap = [(0, k)]
        visited = set()
        max_time = 0

        while heap:
            time, node = heapq.heappop(heap)

            # Skip if we've already found a shorter path to this node
            if node in visited:
                continue

            # Mark as visited and track the max time it took to reach this node
            visited.add(node)
            max_time = max(max_time, time)

            # Explore neighbors
            for neighbor, weight in adj[node]:
                if neighbor not in visited:
                    heapq.heappush(heap, (time + weight, neighbor))

        # If visited count equals n, all nodes were reached
        return max_time if len(visited) == n else -1
