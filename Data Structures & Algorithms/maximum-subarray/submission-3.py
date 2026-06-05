class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        max_so_far = nums[0]

        for i in range(1, len(nums)):
            max_so_far = max(max_so_far + nums[i], nums[i])
            res = max(res, max_so_far)

            if max_so_far < 0:
                max_so_far = 0


        return res
        


        