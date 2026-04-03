# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        small = p if p.val < q.val else q
        large = p if p.val >= q.val else q

        node = root

        while node:
            
            if small.val <= node.val <= large.val:
                return node
            elif node.val > large.val:
                node = node.left
            else:
                node = node.right

            
        