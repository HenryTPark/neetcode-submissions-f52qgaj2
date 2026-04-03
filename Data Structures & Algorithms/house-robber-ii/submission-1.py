class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        def helper(start, end):
            one, two = 0, 0

            for i in range(start, end + 1):
                num = nums[i]

                cur = max(two + num, one)

                two = one
                one = cur

            return one

        n = len(nums)
        return max(helper(0, n - 2), helper(1, n - 1))



        