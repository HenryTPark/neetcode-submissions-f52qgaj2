class Solution:
    def partition(self, s: str) -> list[list[str]]:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j]:
                    if length <= 2 or dp[i + 1][j - 1]:
                        dp[i][j] = True

        result = []
        path = []

        def dfs(start_idx):
            if start_idx == n:
                result.append(path[:])
                return

            for end_idx in range(start_idx, n):
                if dp[start_idx][end_idx]:
                    path.append(s[start_idx : end_idx + 1])
                    dfs(end_idx + 1)
                    path.pop()

        dfs(0)
        return result
                    
