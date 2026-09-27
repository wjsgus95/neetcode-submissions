from functools import lru_cache

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        X, Y = len(matrix), len(matrix[0])

        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]

        @lru_cache
        def recurse(x: int, y: int) -> int:
            result = 1

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < X and 0 <= ny < Y:
                    if matrix[nx][ny] > matrix[x][y]:
                        result = max(result, recurse(nx, ny) + 1)
            
            return result
        
        ans = 1
        for x in range(X):
            for y in range(Y):
                ans = max(ans, recurse(x, y))
        return ans