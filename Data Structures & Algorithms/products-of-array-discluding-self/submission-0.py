class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        running_product = 1
        for i in range(n):
            res[i] *= running_product
            running_product *= nums[i]

        running_product = 1
        for j in range(n - 1, -1, -1):
            res[j] *= running_product
            running_product *= nums[j]

        return res
        