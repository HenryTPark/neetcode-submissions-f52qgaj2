class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # from pacific to inwards
        # from atlantic to inwards
        # find intersections

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        m, n = len(heights), len(heights[0])
        def inbound(r, c):
            return 0 <= r < m and 0 <= c < n

        pacific = set()
        atlantic = set()
        visited = set()

        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0:
                    pacific.add((r, c))
                
                if r == m - 1 or c == n - 1:
                    atlantic.add((r, c))

        def dfs(r, c, o):
            o.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if inbound(nr, nc) and (nr, nc) not in o and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, o)

        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0:
                    dfs(r, c, pacific)
                
                if r == m - 1 or c == n - 1:
                    dfs(r, c, atlantic)

        res = []

        for (r, c) in pacific:
            if (r, c) in atlantic:
                res.append((r, c))

        return res


        