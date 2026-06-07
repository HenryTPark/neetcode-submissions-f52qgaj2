# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        node = root

        while stack or k:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            k -= 1

            if not k:
                return node.val
            
            node = node.right
        