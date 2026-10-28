import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        '''
        visited
        
        time
        start from (0, 0)
        compare the neighboring cells to the current_time
            if current_time is smaller than smallest of the neighboring cells, update time to that min_cell and move to that cell
        
        terminate when you're at the bottom right of the grid

        dijkstra's
        '''
        heap = [(grid[0][0], 0, 0)]

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        m, n = len(grid), len(grid[0])
        visited = set()

        def inbounds(row, col):
            return 0 <= row < m and 0 <= col < n

        while heap:
            time, row, col = heapq.heappop(heap)


            if row == m - 1 and col == n - 1:
                return time

            if (row, col) in visited:
                continue

            visited.add((row, col))


            for dr, dc in directions:
                next_row, next_col = row + dr, col + dc

                if inbounds(next_row, next_col) and (next_row, next_col) not in visited:
                    heapq.heappush(heap, (max(time, grid[next_row][next_col]), next_row, next_col))


        
        