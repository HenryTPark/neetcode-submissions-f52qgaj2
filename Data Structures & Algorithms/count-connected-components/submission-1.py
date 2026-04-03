class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            if node == parent[node]:
                return node

            parent[node] = find(parent[node])
            return parent[node]

        def union(node1, node2):
            group1, group2 = find(node1), find(node2)

            if group1 == group2:
                return False

            if rank[group1] > rank[group2]:
                parent[group2] = group1
                rank[group1] += rank[group2]
            else:
                parent[group1] = group2
                rank[group2] += rank[group1]

            return True

        num_groups = n

        for node1, node2 in edges:
            if union(node1, node2):
                num_groups -= 1

        return num_groups

        

            

        
        