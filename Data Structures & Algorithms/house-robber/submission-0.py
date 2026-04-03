class Solution:
    def rob(self, nums: List[int]) -> int:
        one, two = 0, 0

        for num in nums:
            curr_max = max(two + num, one)

            two = one
            one = curr_max

        return one

        