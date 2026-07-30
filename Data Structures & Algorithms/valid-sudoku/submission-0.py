class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            row_check = set()
            x = 0
            for j in range(9):
                if board[i][j] != '.':
                    x += 1
                    row_check.add(board[i][j])
                    if len(row_check) != x:
                        return False

        for i in range(9):
            col_check = set()
            y = 0
            for j in range(9):
                if board[j][i] != '.':
                    y += 1
                    col_check.add(board[j][i])
                    if len(col_check) != y:
                        return False

        for r in (0, 3, 6):
            for c in (0, 3, 6):
                box_check = set()
                for dr in range(3):
                    for dc in range(3):
                        val = board[r + dr][c + dc]
                        if val != '.':
                            if val in box_check:
                                return False
                            box_check.add(val)

            
        return True