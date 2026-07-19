# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # O(N) Time | O(N) Space
        result = []

        def dfs(node):
            if not node:
                result.append('N')
                return
            
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)

        return ','.join(result)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # O(N) Time | O(N) Space
        values = iter(data.split(','))

        def parse():
            value = next(values)

            if value == 'N':
                return None

            node = TreeNode(int(value))
            node.left = parse()
            node.right = parse()

            return node

        return parse()

        




