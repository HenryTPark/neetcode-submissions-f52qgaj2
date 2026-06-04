class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        def helper(left, right):
            one, two = 0, 0

            for i in range(left, right + 1):
                cur = max(one, two + nums[i])

                two = one
                one = cur

            return one

        return max(helper(0, n - 2), helper(1, n - 1))
        