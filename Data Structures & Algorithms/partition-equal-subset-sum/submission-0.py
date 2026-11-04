class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # O(2 ^ N) Time | O(N) Space
        total = sum(nums)
        n = len(nums)


        if total % 2:
            return False

        target_sum = total // 2

        def dfs(index, running_sum):
            if running_sum == target_sum:
                return True

            if index == n or running_sum > target_sum:
                return False

            return (
                dfs(index + 1, running_sum + nums[index])
                or dfs(index + 1, running_sum)
            )

        return dfs(0, 0)
                
        