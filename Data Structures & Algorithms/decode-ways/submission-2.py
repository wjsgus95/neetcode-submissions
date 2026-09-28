class Solution:
    def numDecodings(self, s: str) -> int:
        S = len(s)

        single = set([str(i) for i in range(1, 10)])
        double = set([str(i) for i in range(10, 27)])

        dp = [None] * (S + 1)
        
        # def recurse(index: int) -> int:
        #     if index == S:
        #         return 1
            
        #     if dp[index] is not None:
        #         return dp[index]
            
        #     ways = 0
        #     if s[index] in single:
        #         ways += recurse(index + 1)
            
        #     if index < S - 1 and s[index:index+2] in double:
        #         ways += recurse(index + 2)
            
        #     dp[index] = ways
        #     return ways

        # return recurse(0)

        # dp[S] = 1
        # for index in range(S - 1, -1, -1):
        #     ways = 0

        #     if s[index] in single:
        #         ways += dp[index + 1]
            
        #     if index < S - 1 and s[index:index+2] in double:
        #         ways += dp[index+2]
            
        #     dp[index] = ways
        
        # return dp[0]

        next1 = 1
        next2 = 0

        for index in range(S - 1, -1, -1):
            ways = 0
            
            if s[index] in single:
                ways += next1
            
            if index < S - 1 and s[index:index+2] in double:
                ways += next2
            
            next2 = next1
            next1 = ways

        return ways