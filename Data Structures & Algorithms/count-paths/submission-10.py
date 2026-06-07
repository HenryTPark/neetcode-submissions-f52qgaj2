class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < n:
            m, n = n, m

        row = [1] * n

        for _ in range(1, m):
            for c in range(1, n):
                row[c] += row[c - 1]

        return row[-1]

