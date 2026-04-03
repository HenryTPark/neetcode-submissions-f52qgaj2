class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {node: set() for node in range(n)}

        for node1, node2 in edges:
            graph[node1].add(node2)
            graph[node2].add(node1)

        visited = set()

        def dfs(node, prev_node):
            if node in visited:
                return False

            visited.add(node)

            for neigh in graph[node]:
                if neigh == prev_node:
                    continue 
                if not dfs(neigh, node):
                    return False

            return True

        return dfs(0, -1) and len(visited) == n
        