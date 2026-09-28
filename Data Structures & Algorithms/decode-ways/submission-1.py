class Solution:
    def numDecodings(self, s: str) -> int:
        S = len(s)

        single = set([str(i) for i in range(1, 10)])
        double = set([str(i) for i in range(10, 27)])

        dp = [None] * (S + 1)
        
        def recurse(index: int) -> int:
            if index > S:
                return 0
            
            if index == S:
                return 1
            
            if dp[index] is not None:
                return dp[index]
            
            ways = 0
            if s[index] in single:
                ways += recurse(index + 1)
            
            if index < S - 1 and s[index:index+2] in double:
                ways += recurse(index + 2)
            
            dp[index] = ways
            return ways
        
        return recurse(0)

