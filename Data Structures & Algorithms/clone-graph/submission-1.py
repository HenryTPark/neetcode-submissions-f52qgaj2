"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # O(V + E) Time | O(V + E) Space
        node_to_copy = { None: None }

        def dfs(node):
            if node in node_to_copy:
                return node_to_copy[node]
            
            copy = Node(node.val)
            node_to_copy[node] = copy

            for neighbor in node.neighbors:
                copy_neighbor = dfs(neighbor)

                copy.neighbors.append(copy_neighbor)
            
            return copy
        
        dfs(node)

        return node_to_copy[node]
        