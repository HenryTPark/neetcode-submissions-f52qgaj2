# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.pre_idx = 0
        val_to_idx = {val:idx for idx, val in enumerate(inorder)}

        def array_to_tree(left, right):
            if left > right:
                return None

            node_val = preorder[self.pre_idx]
            node = TreeNode(node_val)
            self.pre_idx += 1

            inorder_idx = val_to_idx[node_val]

            node.left = array_to_tree(left, inorder_idx - 1)
            node.right = array_to_tree(inorder_idx + 1, right)

            return node

        return array_to_tree(0, len(preorder) - 1)

        