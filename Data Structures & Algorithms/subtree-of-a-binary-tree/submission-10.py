# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # O(N) Time | O(H) Space
        if not root or not subRoot:
            return not root and not subRoot

        def is_same_tree(tree1, tree2):
            if not tree1 or not tree2:
                return not tree1 and not tree2
            
            if tree1.val != tree2.val:
                return False
            
            return is_same_tree(tree1.left, tree2.left) and is_same_tree(tree1.right, tree2.right)
        

        if is_same_tree(root, subRoot):
            return True


        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        