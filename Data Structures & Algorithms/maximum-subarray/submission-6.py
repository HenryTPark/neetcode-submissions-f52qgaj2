class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = float('-inf')

        running_sum = 0

        for num in nums:
            running_sum += num

            result = max(running_sum, result)

            if running_sum < 0:
                running_sum = 0
        
        return result
        