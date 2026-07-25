import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < n:
            m, n = n, m

        prev_row = [1] * n

        for row in range(1, m):
            current_row = [1] * n

            for col in range(1, n):
                current_row[col] = prev_row[col] + current_row[col - 1]
            
            prev_row = current_row

        return prev_row[-1]

        
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(m + n - 2, min(m - 1, n - 1))

        