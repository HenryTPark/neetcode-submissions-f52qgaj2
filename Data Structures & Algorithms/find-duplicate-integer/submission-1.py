from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # O(N log N) Time | O(1) Space
        # N: length of the nums array
        """
        Finds the duplicate by binary searching the range of possible integers.
        """
        low = 1
        high = len(nums) - 1
        
        while low < high:
            mid = (low + high) // 2
            count = 0
            
            # Count how many numbers in the array are less than or equal to mid
            for num in nums:
                if num <= mid:
                    count += 1
            
            # Pigeonhole Principle: if count > mid, the duplicate is in the lower half
            if count > mid:
                high = mid
            else:
                low = mid + 1
                
        return low