class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        X, Y = len(matrix), len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        for x in range(X):
            if matrix[x][0] == 0:
                first_col_zero = True
        
        for y in range(Y):
            if matrix[0][y] == 0:
                first_row_zero = True
        
        for x in range(1, X):
            for y in range(1, Y):
                if matrix[x][y] == 0:
                    matrix[0][y] = 0
                    matrix[x][0] = 0
        
        for x in range(1, X):
            for y in range(1, Y):
                if matrix[0][y] == 0:
                    matrix[x][y] = 0
                if matrix[x][0] == 0:
                    matrix[x][y] = 0
        
        if first_row_zero:
            for y in range(Y):
                matrix[0][y] = 0
        
        if first_col_zero:
            for x in range(X):
                matrix[x][0] = 0
                
        