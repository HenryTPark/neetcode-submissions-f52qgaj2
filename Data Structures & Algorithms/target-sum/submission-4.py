class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}        
        n = len(nums)
        
        def dfs(index, total):
            if index == n:
                return 1 if total == target else 0

            if (index, total) in memo:
                return memo[(index, total)]

            add_path = dfs(index + 1, total + nums[index])
            sub_path = dfs(index + 1, total - nums[index])

            memo[(index, total)] = add_path + sub_path

            return memo[(index, total)]

        return dfs(0, 0)