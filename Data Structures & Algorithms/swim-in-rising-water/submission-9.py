class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        # O(N^2 * log(N)) Time | O(N^2) Space
        # N: number of rows/cols in the square grid

        """
        Binary searches the answer space and verifies if a path is possible using DFS.
        """
        n = len(grid)

        def has_path(target_time):
            # Cannot even start if the first cell requires more time
            if grid[0][0] > target_time:
                return False

            stack = [(0, 0)]
            visited = {(0, 0)}
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

            while stack:
                r, c = stack.pop()
                if r == n - 1 and c == n - 1:
                    return True

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                        # Only traverse if water level is high enough for the neighbor
                        if grid[nr][nc] <= target_time:
                            visited.add((nr, nc))
                            stack.append((nr, nc))
            return False

        # Binary Search bounds
        left, right = grid[0][0], (n * n) - 1
        ans = right

        while left <= right:
            mid = (left + right) // 2
            if has_path(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans