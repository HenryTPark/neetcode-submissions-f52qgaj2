class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        top = 0
        bot = m - 1
        left = 0
        right = n - 1

        res = []
        while top <= bot and left <= right:
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            
            for row in range(top + 1, bot + 1):
                res.append(matrix[row][right])

            if top < bot:
                for col in range(right - 1, left - 1, -1):
                    res.append(matrix[bot][col])

            if left < right:
                for row in range(bot - 1, top, -1):
                    res.append(matrix[row][left])

            top += 1
            bot -= 1
            left += 1
            right -= 1

        return res
            
        