# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val:idx for idx, val in enumerate(inorder)}
        self.i = 0

        def helper(left, right):
            if left > right:
                return

            node = TreeNode(preorder[self.i])
            inorder_idx = inorder_map[node.val]

            self.i += 1

            node.left = helper(left, inorder_idx - 1)
            node.right = helper(inorder_idx + 1, right)

            return node

        return helper(0, len(preorder) - 1)

        