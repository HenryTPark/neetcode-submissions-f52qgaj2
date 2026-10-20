import heapq

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        WATER, TREASURE, LAND = -1, 0, 2**31 - 1
        m, n = len(grid), len(grid[0])

        def inbounds(row, col):
            return 0 <= row < m and 0 <= col < n

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        heap = []

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    heap.append((0, row, col))

        heapq.heapify(heap)

        while heap:
            dist, row, col = heapq.heappop(heap)

            for dr, dc in directions:
                next_row, next_col = row + dr, col + dc

                if (
                    inbounds(next_row, next_col)
                    and grid[next_row][next_col] > dist + 1
                ):
                    grid[next_row][next_col] = dist + 1
                    heapq.heappush(heap, (dist + 1, next_row, next_col))

        # return grid
        

        

        
        