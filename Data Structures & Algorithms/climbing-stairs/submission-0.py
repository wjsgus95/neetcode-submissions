class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [None] * (n + 1)

        def recurse(i: int) -> int:
            if dp[i] is not None:
                return dp[i]
            
            if i == 0:
                return 0
            
            if i == 1:
                return 1
            
            if i == 2:
                return 2
            
            dp[i] = recurse(i - 2) + recurse(i - 1)
            return dp[i]
        
        return recurse(n)