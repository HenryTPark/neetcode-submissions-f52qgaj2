class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        result = nums[0]
        min_prod = nums[0]
        max_prod = nums[0]

        n = len(nums)
        for i in range(1, n):
            if nums[i] < 0:
                min_prod, max_prod = max_prod, min_prod

            max_prod = max(nums[i], max_prod * nums[i])
            min_prod = min(nums[i], min_prod * nums[i])

            result = max(result, max_prod)

        return result



        