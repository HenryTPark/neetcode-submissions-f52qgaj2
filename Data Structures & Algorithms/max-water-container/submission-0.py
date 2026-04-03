class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # O(N) Time | O(1) Space
        res = 0
        n = len(heights)
        left, right = 0, n - 1

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])

            res = max(res, width * height)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return res
        