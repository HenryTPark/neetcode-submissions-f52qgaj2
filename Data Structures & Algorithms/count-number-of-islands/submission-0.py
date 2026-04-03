from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # O(MN) Time | O(min(M, N)) Space
        # M: number of rows, N: number of cols
        LAND, WATER = '1', '0'
        m, n = len(grid), len(grid[0])

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def inbounds(r, c):
            return 0 <= r < m and 0 <= c < n

        def bfs(r, c):
            queue = deque([(r, c)])
            grid[r][c] = WATER

            while queue:
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if inbounds(nr, nc) and grid[nr][nc] == LAND:
                        grid[nr][nc] = WATER
                        queue.append((nr, nc))
        
        num_islands = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == LAND:
                    num_islands += 1
                    bfs(r, c)

        return num_islands


        