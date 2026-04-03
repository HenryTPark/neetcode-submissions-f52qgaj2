class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific_set = set()
        atlantic_set = set()

        def inbounds(r, c):
            return 0 <= r < m and 0 <= c < n

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def dfs(r, c, o):
            o.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if inbounds(nr, nc) and (nr, nc) not in o and heights[r][c] <= heights[nr][nc]:
                    dfs(nr, nc, o)

        for r in range(m):
            dfs(r, 0, pacific_set)
            dfs(r, n - 1, atlantic_set)

        for c in range(n):
            dfs(0, c, pacific_set)
            dfs(m - 1, c, atlantic_set)

        return list(pacific_set.intersection(atlantic_set))


        
        