class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        max_so_far = 0

        for num in nums:
            max_so_far += num

            res = max(res, max_so_far)
            
            if max_so_far < 0:
                max_so_far = 0

        return res
        