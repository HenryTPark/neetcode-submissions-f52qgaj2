# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, largest):
            if not node:
                return 0

            is_good = 1 if node.val >= largest else 0

            largest = max(node.val, largest)

            left_count = dfs(node.left, largest)
            right_count = dfs(node.right, largest)

            return is_good + left_count + right_count

        return dfs(root, -float('inf'))


        