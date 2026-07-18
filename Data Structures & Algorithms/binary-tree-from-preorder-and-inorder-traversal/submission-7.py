# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # O(N) Time | O(N) Space
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        preorder_iter = iter(preorder)

        def traverse(left, right):
            if left > right:
                return

            val = next(preorder_iter)
            
            node = TreeNode(val)
            inorder_idx = inorder_map[val]
            node.left = traverse(left, inorder_idx - 1)
            node.right = traverse(inorder_idx + 1, right)

            return node

        return traverse(0, len(preorder) - 1)
            
        
        