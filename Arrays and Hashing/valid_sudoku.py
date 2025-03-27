class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        print(board)
        for i in range(9):
            visited = set()
            for j in range(9):
                if board[i][j].isnumeric() and board[i][j] in visited:
                    print("failed row")
                    return False
                else: 
                    visited.add(board[i][j])
        
        for j in range(9):
            visited = set()
            for i in range(9):
                if board[i][j].isnumeric() and board[i][j] in visited:
                    print("failed col")
                    return False
                else: 
                    visited.add(board[i][j])
        
        def checkSubBoxes(row, col):
            visited = set()
            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    if board[i][j].isnumeric() and board[i][j] in visited:
                        print(visited, board[i][j])
                        return True
                    else: 
                        visited.add(board[i][j])
            return False
        
        for i in range(3):
            for j in range(3):
                if checkSubBoxes(i*3, j*3):
                    print("failed subbox", i*3, j*3)
                    return False
        return True

