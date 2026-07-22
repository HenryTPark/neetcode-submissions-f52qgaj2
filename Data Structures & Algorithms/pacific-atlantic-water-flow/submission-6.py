class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # O(MN) Time | O(MN) Space
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        m, n = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        def inbounds(row, col):
            return 0 <= row < m and 0 <= col < n

        def dfs(row, col, ocean):
            ocean.add((row, col))

            for dr, dc in directions:
                next_row, next_col = row + dr, col + dc

                if (
                    inbounds(next_row, next_col)
                    and (next_row, next_col) not in ocean
                    and heights[next_row][next_col] >= heights[row][col]
                ):
                    dfs(next_row, next_col, ocean)
        
        for row in range(m):
            dfs(row, 0, pacific)
            dfs(row, n - 1, atlantic)
        
        for col in range(n):
            dfs(0, col, pacific)
            dfs(m - 1, col, atlantic)


        return list(map(lambda x: list(x), pacific & atlantic))
        


        
        