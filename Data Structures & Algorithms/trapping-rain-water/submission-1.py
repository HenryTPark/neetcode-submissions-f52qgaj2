class Solution:
    def trap(self, heights: list[int]) -> int:
        # O(N) Time | O(1) Space
        # N: number of elevations in the heights array
        if not heights:
            return 0

        left, right = 0, len(heights) - 1
        max_left, max_right = heights[left], heights[right]
        total_water = 0

        while left < right:
            if max_left < max_right:
                left += 1
                max_left = max(max_left, heights[left])
                total_water += max_left - heights[left]
            else:
                right -= 1
                max_right = max(max_right, heights[right])
                total_water += max_right - heights[right]

        return total_water