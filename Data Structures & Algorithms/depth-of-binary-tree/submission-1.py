# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self._get_max_depth(root, 0)

    def _get_max_depth(self, node, depth):
        if not node:
            return depth

        left_depth = self._get_max_depth(node.left, depth)
        right_depth = self._get_max_depth(node.right, depth)

        return max(left_depth, right_depth) + 1
        