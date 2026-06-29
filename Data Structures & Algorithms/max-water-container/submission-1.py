class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # O(N) Time | O(1) Space
        n = len(heights)
        left, right = 0, n - 1
        max_area = 0

        while left < right:
            width = right - left

            left_height = heights[left]
            right_height = heights[right]
            height = min(left_height, right_height)
            
            max_area = max(max_area, width * height)

            if left_height < right_height:
                left += 1
            else:
                right -= 1


        return max_area
        