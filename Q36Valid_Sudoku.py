class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return (self.valid_row(board) and self.valid_col(board) and self.valid_square(board))
    
    def valid_row(self, board):
        for row in board:
            res = [r for r in row if r != '.']
            if len(set(res)) != len(res):
                return False
        return True
            
    def valid_col(self, board):
        for row in zip(*board):
            res = [r for r in row if r != '.']
            if len(set(res)) != len(res):
                return False
        return True
            
    def valid_square(self, board):
        for i in range(0,7,3):
            for j in range(0, 7, 3):
                med = [board[a][b] for a in range(i, i+3) for b in range(j, j+3)]
                res = [r for r in med if r != '.']
                if len(set(res)) != len(res):
                    return False
        return True
