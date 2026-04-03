class Solution:
    def findMin(self, nums: List[int]) -> int:
        # O(log N) Time | O(1) Space
        # N: number of elements in nums
        
        # 1. Handle fully sorted or single element case immediately
        if nums[0] <= nums[-1]:
            return nums[0]
            
        l, r = 0, len(nums) - 1
        
        while l < r:
            m = (l + r) // 2
            
            # If mid is part of the left sorted sequence (larger values),
            # the pivot (min) must be to the right.
            if nums[m] >= nums[0]:
                l = m + 1
            # If mid is part of the right sorted sequence (smaller values),
            # the pivot is at m or to the left.
            else:
                r = m
                
        return nums[l]