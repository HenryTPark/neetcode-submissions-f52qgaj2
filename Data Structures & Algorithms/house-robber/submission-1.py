class Solution:
    def rob(self, nums: List[int]) -> int:
        two = 0
        one = 0

        for num in nums:
            cur = max(two + num, one)

            two = one
            one = cur

        return one