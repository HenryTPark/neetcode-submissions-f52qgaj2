class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])

        top, bot = 0, m - 1
        left, right = 0, n - 1

        result = []


        while top <= bot and left <= right:
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            
            for row in range(top + 1, bot + 1):
                result.append(matrix[row][right])
            
            if top < bot:
                for col in range(right - 1, left - 1, -1):
                    result.append(matrix[bot][col])
            
            if left < right:
                for row in range(bot - 1, top, -1):
                    result.append(matrix[row][left])
            
            top += 1
            bot -= 1
            left += 1
            right -= 1
        
        return result


        