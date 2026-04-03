class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:
            return True

        graph = {node: set() for node in range(n)}

        for node1, node2 in edges:
            graph[node1].add(node2)
            graph[node2].add(node1)

        visited_nodes = set()
        
        def has_no_cycles(node, parent_node):
            if node in visited_nodes:
                return False

            visited_nodes.add(node)

            for neighbor in graph[node]:
                if neighbor == parent_node:
                    continue

                if not has_no_cycles(neighbor, node):
                    return False

            return True

        return has_no_cycles(0, -1) and len(visited_nodes) == n

