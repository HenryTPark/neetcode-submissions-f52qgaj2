class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0

            left_sum = max(dfs(node.left), 0)
            right_sum = max(dfs(node.right), 0)

            self.max_sum = max(self.max_sum, left_sum + right_sum + node.val)

            return node.val + max(left_sum, right_sum)
        dfs(root)
        return self.max_sum