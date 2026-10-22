from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        minutes = 0
        
        def inbounds(row, col):
            return 0 <= row < m and 0 <= col < n
        
        queue = deque()

        fresh_count = 0
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    fresh_count += 1
                elif grid[row][col] == 2:
                    queue.append((row, col))
        
        while queue and fresh_count:

            for _ in range(len(queue)):
                row, col = queue.popleft()

                for dr, dc in directions:
                    next_row, next_col = row + dr, col + dc

                    if (
                        inbounds(next_row, next_col)
                        and grid[next_row][next_col] == 1
                    ):
                        fresh_count -= 1
                        grid[next_row][next_col] = 2
                        queue.append((next_row, next_col))

            minutes += 1

        return minutes if fresh_count == 0 else -1




        