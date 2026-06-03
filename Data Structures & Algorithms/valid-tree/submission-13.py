class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid tree: has no cycle
        adj_list = defaultdict(list)

        for v, e in edges:
            adj_list[v].append(e)
            adj_list[e].append(v)

        visited = set()

        def has_cycle(node, parent):
            if node in visited:
                return True

            visited.add(node)

            for neighbor in adj_list[node]:
                if neighbor is parent:
                    continue

                if has_cycle(neighbor, node):
                    return True

            return False
            

        if has_cycle(0, -1):
            return False

        return len(visited) == n

        