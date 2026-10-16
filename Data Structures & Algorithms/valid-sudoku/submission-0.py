class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #testing row and column:
        for i in range(9):
            row = []
            column = []
            for j in range(9):
                if board[i][j] != ".":
                    row.append(board[i][j])
                if board[j][i] != ".":
                    column.append(board[j][i])
            if len(set(row)) != len(row) or len(set(column)) != len(column):
                return False
        
        #testing 3*3 subsquare

        for x in range(3):
            for y in range(3):
                subsquare = []
                for i in range(3):
                    for j in range(3):
                        coordinate1 = 3*x+i 
                        coordinate2 = 3*y+j
                        if board[coordinate1][coordinate2] != ".":
                            subsquare.append(board[coordinate1][coordinate2])
                if len(set(subsquare)) != len(subsquare):
                    return False
        return True

            