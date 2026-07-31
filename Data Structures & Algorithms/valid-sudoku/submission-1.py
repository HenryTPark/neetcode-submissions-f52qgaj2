from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        row + col
        - <= 2 -> 0
        - 2 <= 5 -> 1
        - 5 <= 8 -> 2
        - 


        0 [0 1 2 3 4 5 6 7 8]
        1 [0 1 2 3 4 5 6 7 8]
        2 [0 1 2 3 4 5 6 7 8]
        3 [0 1 2 3 4 5 6 7 8]
        4 [0 1 2 3 4 5 6 7 8]
        5 [0 1 2 3 4 5 6 7 8]
        6 [0 1 2 3 4 5 6 7 8]
        7 [0 1 2 3 4 5 6 7 8]
        8 [0 1 2 3 4 5 6 7 8]

        (row // 3, col // 3) -> (0, 0)
        (1, 0)
        
        '''
        grids = defaultdict(set)
        rows = defaultdict(set)
        cols = defaultdict(set)
        n = len(board)

        for row in range(n):
            for col in range(n):
                value = board[row][col]
                
                if value == '.':
                    continue

                grid_id = (row // 3, col // 3)
                
                if (
                    value in grids[grid_id]
                    or value in rows[row]
                    or value in cols[col]
                ):
                    return False

                rows[row].add(value)
                cols[col].add(value)
                grids[grid_id].add(value)

        return True
                



                

                
        
        pass
        