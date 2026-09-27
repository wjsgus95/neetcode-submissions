class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[None] * n for _ in range(m)]

        def recurse(x: int, y: int) -> int:
            if dp[x][y] is not None:
                return dp[x][y]
            
            if x == m - 1 and y == n - 1:
                return 1
            
            result = 0
            if y + 1 <= n - 1:
                result += recurse(x, y + 1)
            if x + 1 <= m - 1:
                result += recurse(x + 1, y)
            
            dp[x][y] = result
            return result
        
        return recurse(0, 0)