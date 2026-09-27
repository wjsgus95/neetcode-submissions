class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)

        def sequence():
            for x in range(N // 2):
                for y in range(x, N - x - 1):
                    yield x, y
        
        def swap(base_x: int, base_y: int):
            end = N - 1
            matrix[x][y], matrix[y][end-x], matrix[end-x][end-y], matrix[end-y][x] = matrix[end-y][x], matrix[x][y], matrix[y][end-x], matrix[end-x][end-y]
        
        for x, y in sequence():
            swap(x, y)
        
        