# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(node):
            if not node:
                res.append('N')
                return
            
            val = str(node.val)
            res.append(val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ','.join(res)



        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(',')
        self.i = 0
        n = len(vals)

        def dfs():
            if self.i >= n:
                return
            if vals[self.i] == 'N':
                self.i += 1
                return None

            val = vals[self.i]
            node = TreeNode(val)
            self.i += 1

            node.left = dfs()
            node.right = dfs()

            return node
        
        return dfs()

