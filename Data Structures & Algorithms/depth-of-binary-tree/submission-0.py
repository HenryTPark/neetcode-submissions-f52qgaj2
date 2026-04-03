# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
diameter: left_height + right_height





'''

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, depth):
            if not node:
                return 0

            left_depth = dfs(node.left, depth)
            right_depth = dfs(node.right, depth)

            return max(left_depth, right_depth) + 1

        return dfs(root, 0)

        