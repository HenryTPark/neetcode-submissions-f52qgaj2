class Solution:
    def rob(self, nums: List[int]) -> int:
        # O(N) Time | O(1) Space
        if len(nums) == 1:
            return nums[0]

        def helper(left, right):
            last, second_last = 0, 0

            for i in range(left, right + 1):
                temp = max(second_last + nums[i], last)

                second_last = last
                last = temp

            return last

        n = len(nums)
        return max(helper(0, n - 2), helper(1, n - 1))

                
        