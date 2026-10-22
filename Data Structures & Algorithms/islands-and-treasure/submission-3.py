from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        queue = deque()

        def inbounds(row, col):
            return 0 <= row < m and 0 <= col < n

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    queue.append((row, col))

        while queue:
            row, col = queue.popleft()

            for dr, dc in directions:
                next_row, next_col = row + dr, col + dc

                if (
                    inbounds(next_row, next_col)
                    and grid[next_row][next_col] > grid[row][col] + 1
                ):
                    grid[next_row][next_col] = grid[row][col] + 1
                    queue.append((next_row, next_col))

        