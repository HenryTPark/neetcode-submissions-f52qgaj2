from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # O(N) Time | O(N) Total Space | O(W) Aux Space
        # W: largest width of a level | N: total number of nodes
        if not root:
            return []
        
        queue = deque([root])
        result = []

        while queue:
            queue_length = len(queue)
            level = []
            
            for _ in range(queue_length):
                node = queue.popleft()

                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level:
                result.append(level)

        return result


            
        


        