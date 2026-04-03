class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        m, n = len(heights), len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def inbounds(row, col):
            return 0 <= row < m and 0 <= col < n

        def dfs_uphill(row, col, reachable_set):
            reachable_set.add((row, col))

            for dr, dc in directions:
                next_row, next_col = row + dr, col + dc

                if (
                    inbounds(next_row, next_col)
                    and (next_row, next_col) not in reachable_set
                    and heights[next_row][next_col] >= heights[row][col]
                ):
                    dfs_uphill(next_row, next_col, reachable_set)

        for row in range(m):
            dfs_uphill(row, 0, pacific_reachable)
            dfs_uphill(row, n - 1, atlantic_reachable)

        for col in range(n):
            dfs_uphill(0, col, pacific_reachable)
            dfs_uphill(m - 1, col, atlantic_reachable)

        return list(pacific_reachable.intersection(atlantic_reachable))

