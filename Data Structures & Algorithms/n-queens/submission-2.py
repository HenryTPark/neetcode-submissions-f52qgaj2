class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [['.'] * n for _ in range(n)]

        cols = set()
        pos_diags = set()
        neg_diags = set()

        def backtrack(row):
            if row == n:
                result.append([''.join(r) for r in board])
                return

            for col in range(n):
                if (
                    col in cols
                    or (row + col) in neg_diags
                    or (row - col) in pos_diags
                ):
                    continue
                
                cols.add(col)
                pos_diags.add(row - col)
                neg_diags.add(row + col)
                board[row][col] = 'Q'

                backtrack(row + 1)
                cols.remove(col)
                pos_diags.remove(row - col)
                neg_diags.remove(row + col)
                board[row][col] = '.'

        backtrack(0)
        return result


                



        