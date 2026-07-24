from collections import defaultdict, deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        graph = defaultdict(list)
        degree = {node: 0 for node in range(n)}

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

            degree[u] += 1
            degree[v] += 1
        
        queue = deque([node for node in degree if degree[node] <= 1])
        nodes_visited = 0

        while queue:
            node = queue.popleft()
            nodes_visited += 1

            for neighbor in graph[node]:
                degree[neighbor] -= 1

                if degree[neighbor] == 1:
                    queue.append(neighbor)
            
        return nodes_visited == n
        