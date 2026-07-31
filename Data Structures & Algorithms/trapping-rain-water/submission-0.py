class Solution:
    def trap(self, heights: List[int]) -> int:
        # O(N) Time | O(1) Space
        if not heights:
            return 0

        n = len(heights)

        left, right = 0, n - 1

        max_area = 0
        left_height, right_height = heights[left], heights[right]

        while left <= right:
            left_height = max(left_height, heights[left])
            right_height = max(right_height, heights[right])
            height = min(left_height, right_height)
            
            if left_height < right_height:
                max_area += (height - heights[left])
                left += 1
            else:
                max_area += (height - heights[right])
                right -= 1

        return max_area

            
            

        



        
        