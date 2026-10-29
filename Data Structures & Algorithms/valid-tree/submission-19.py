class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        parent = [i for i in range(n)]

        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node])
            
            return parent[node]

        def union(node1, node2):
            root1, root2 = find(node1), find(node2)

            if root1 == root2:
                return False

            parent[root1] = root2

            return True
        
        for u, v in edges:
            if not union(u, v):
                return False
            
        return True
        