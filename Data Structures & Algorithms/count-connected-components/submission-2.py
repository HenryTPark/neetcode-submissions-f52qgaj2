class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # union entire grp
        # return the number of groups...?
        parent = { node: node for node in range(n) }

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            
            return parent[node]

        def union(u, v):
            root1, root2 = find(u), find(v)

            if root1 != root2:
                parent[root2] = root1
                return 1

            return 0

        
        result = n

        for u, v in edges:
            result -= union(u, v)
        
        return result
            


        