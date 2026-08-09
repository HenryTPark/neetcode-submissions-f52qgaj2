class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # O(Log(MN)) Time | O(1) Space
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            mid = left + (right - left) // 2

            row = mid // cols
            col = mid % cols

            value = matrix[row][col]

            if value == target:
                return True
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1
            
        return False
        