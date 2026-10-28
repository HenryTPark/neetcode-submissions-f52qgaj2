class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)

        def has_path(target_time):
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
                        if grid[nr][nc] <= target_time:
                            visited.add((nr, nc))
                            stack.append((nr, nc))

            return False

        left, right = grid[0][0], n ** 2 - 1
        result = right

        while left <= right:
            mid = (left + right) // 2

            if has_path(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result

