"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        node_to_copy = {None:None}

        def dfs(node):
            if node in node_to_copy:
                return node_to_copy[node]

            copy_node = Node(node.val)
            node_to_copy[node] = copy_node

            for neighbor_node in node.neighbors:
                copy_neighbor = dfs(neighbor_node)
                copy_node.neighbors.append(copy_neighbor)

            return copy_node

        return dfs(node)
            


                




        