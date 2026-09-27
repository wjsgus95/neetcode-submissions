class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        X, Y = 3, 3
        N = 9

        def validate_row(x: int) -> bool:
            nums = set()
            for y in range(N):
                if board[x][y] == '.':
                    continue
                
                if board[x][y] in nums:
                    return False
                
                nums.add(board[x][y])
            return True
        
        def validate_col(y: int) -> bool:
            nums = set()
            for x in range(N):
                if board[x][y] == '.':
                    continue
                
                if board[x][y] in nums:
                    return False
                
                nums.add(board[x][y])
            return True
        
        def validate_cell(x: int, y: int) -> bool:
            nums = set()
            for dx in range(X):
                for dy in range(Y):
                    nx, ny = x + dx, y + dy
                    if board[nx][ny] == '.':
                        continue
                    
                    if board[nx][ny] in nums:
                        return False
                    
                    nums.add(board[nx][ny])
            
            return True
        
        for i in range(N):
            if not validate_row(i):
                return False
            
            if not validate_col(i):
                return False
        
        for x in range(0, N, X):
            for y in range(0, N, Y):
                if not validate_cell(x, y):
                    return False
        
        return True

        
        