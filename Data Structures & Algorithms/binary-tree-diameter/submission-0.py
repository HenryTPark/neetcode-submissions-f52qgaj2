# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0
        def dfs(node):
            nonlocal result

            if not node:
                return -1

            left_height = max(dfs(node.left), 0)
            right_height = max(dfs(node.right), 0)

            result = max(result, left_height + right_height)

            return max(left_height, right_height) + 1


        dfs(root)

        return result
        