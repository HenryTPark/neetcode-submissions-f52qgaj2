class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n
        components_count = n

        def find_root(node):
            if node == parent[node]:
                return node

            parent[node] = find_root(parent[node])
            return parent[node]

        def union_nodes(node1, node2):
            root1 = find_root(node1)
            root2 = find_root(node2)

            if root1 == root2:
                return False

            if rank[root1] > rank[root2]:
                parent[root2] = root1
                rank[root1] += rank[root2]
            else:
                parent[root1] = root2
                rank[root2] += rank[root1]
            
            return True

        for node1, node2 in edges:
            if union_nodes(node1, node2):
                components_count -= 1

        return components_count
