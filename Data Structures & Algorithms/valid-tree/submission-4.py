class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {node:set() for node in range(n)}

        for source, target in edges:
            adjList[source].add(target)
            adjList[target].add(source)

        visited = set()

        def dfs(node, prev_node):
            if node in visited:
                return False

            visited.add(node)

            for target in adjList[node]:
                if target == prev_node:
                    continue
                
                if not dfs(target, node):
                    return False

            return True

        return dfs(0, -1) and len(visited) == n





        


        