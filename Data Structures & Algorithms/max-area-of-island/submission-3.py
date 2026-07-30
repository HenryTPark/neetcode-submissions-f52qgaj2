from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # O(MN) Time | O(MN) Space
        visited = set()
        m, n = len(grid), len(grid[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        max_area = 0

        def inbounds(row, col):
            return 0 <= row < m and 0 <= col < n

        def bfs(start_row, start_col):
            queue = deque([(start_row, start_col)])
            area = 0
            visited.add((start_row, start_col))

            while queue:
                row, col = queue.popleft()

                area += 1

                for dr, dc in directions:
                    next_row, next_col = row + dr, col + dc

                    if (
                        inbounds(next_row, next_col)
                        and (next_row, next_col) not in visited
                        and grid[next_row][next_col] == 1
                    ):
                        visited.add((next_row, next_col))
                        queue.append((next_row, next_col))

            return area

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1 and (row, col) not in visited:
                    max_area = max(max_area, bfs(row, col))

        return max_area








        
        