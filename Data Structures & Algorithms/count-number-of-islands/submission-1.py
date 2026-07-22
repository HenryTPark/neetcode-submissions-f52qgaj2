class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def inbounds(row, col):
            return 0 <= row < m and 0 <= col < n

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def dfs(row, col):
            grid[row][col] = '0'

            for dr, dc in directions:
                next_row, next_col = row + dr, col + dc

                if (
                    inbounds(next_row, next_col)
                    and grid[next_row][next_col] == '1'
                ):
                    dfs(next_row, next_col)
        
        result = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1':
                    dfs(row, col)
                    result += 1
        
        return result

        