class Solution:
    def rob(self, nums: List[int]) -> int:
        # O(N) Time | O(1) Space
        one, two = 0, 0

        for num in nums:
            cur = max(one, two + num)

            two = one
            one = cur

        return one
        