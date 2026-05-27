# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.pre_idx = 0
        inorder_val_to_idx = {val:idx for idx, val in enumerate(inorder)}

        def helper(left, right):
            if left > right:
                return

            node = TreeNode(preorder[self.pre_idx])
            inorder_idx = inorder_val_to_idx[node.val]
            
            self.pre_idx += 1

            node.left = helper(left, inorder_idx - 1)
            node.right = helper(inorder_idx + 1, right)

            return node
        
        return helper(0, len(preorder) - 1)
        
        