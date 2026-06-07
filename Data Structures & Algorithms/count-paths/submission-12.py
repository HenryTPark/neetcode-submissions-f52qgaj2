class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < n:
            m, n = n, m

        ROW = [1] * n

        for r in range(1, m):
            for c in range(1, n):
                ROW[c] += ROW[c - 1]

        return ROW[-1]


        
        