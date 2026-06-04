class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj_list = defaultdict(list)

        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        visited = set()

        def has_cycle(node, parent):
            if node in visited:
                return True

            visited.add(node)

            for neighbor in adj_list[node]:
                if neighbor == parent:
                    continue

                if has_cycle(neighbor, node):
                    return True

            return False

        return not has_cycle(0, -1) and len(visited) == n

            

        
        