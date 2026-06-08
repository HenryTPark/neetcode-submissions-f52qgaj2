class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        running_product = 1
        res = [1] * n

        # [1 2 4 6]
        # [1 1 1 1]
        for i in range(n):
            res[i] *= running_product
            running_product *= nums[i]

        running_product = 1

        for j in reversed(range(n)):
            res[j] *= running_product
            running_product *= nums[j]

        return res
        