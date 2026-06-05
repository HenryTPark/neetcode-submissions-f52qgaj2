class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        cur_min, cur_max, res = [nums[0]] * 3

        for i in range(1, len(nums)):
            if nums[i] < 0:
                cur_min, cur_max = cur_max, cur_min

            cur_min = min(nums[i], cur_min * nums[i])
            cur_max = max(nums[i], cur_max * nums[i])

            res = max(res, cur_max)

        return res

        