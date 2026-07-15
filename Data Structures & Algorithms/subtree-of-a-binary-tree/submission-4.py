# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return root is None and subRoot is None

        if self._is_same_tree(root, subRoot):
            return True

        return (
            self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )
        
        
    def _is_same_tree(self, tree, sub_tree):
        if not tree or not sub_tree:
            return tree is None and sub_tree is None

        if tree.val != sub_tree.val:
            return False

        return (
            self._is_same_tree(tree.left, sub_tree.left) 
            and self._is_same_tree(tree.right, sub_tree.right)
        )
        