class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # O(N) Time | O(1) Space
        result = float('-inf')

        running_sum = 0

        for num in nums:
            running_sum += num

            result = max(running_sum, result)

            if running_sum < 0:
                running_sum = 0
        
        return result
        