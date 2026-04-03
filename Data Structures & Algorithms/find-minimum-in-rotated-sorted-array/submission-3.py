class Solution:
    def findMin(self, nums: List[int]) -> int:
        # O(log N) Time | O(1) Space
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            # If mid is greater than right, the min must be to the right
            if nums[m] > nums[r]:
                l = m + 1
            # Otherwise, the min is at m or to the left
            else:
                r = m

        return nums[l]