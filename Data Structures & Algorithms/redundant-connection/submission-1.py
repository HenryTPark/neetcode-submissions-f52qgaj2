class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [1 for _ in range(len(edges) + 1)]

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            
            return parent[node]

        
        def union(node1, node2):
            root1, root2 = find(node1), find(node2)

            if root1 == root2:
                return False

            if rank[root1] > rank[root2]:
                parent[root2] = root1
                rank[root1] += rank[root2]
            else:
                parent[root1] = root2
                rank[root2] += rank[root1]

            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]

        return []
        