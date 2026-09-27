class Solution:
    def countBits(self, n: int) -> List[int]:
        # dp = [None] * (n + 1)
        # dp[0] = 0

        # def recurse(k: int) -> int:
        #     if k == 0:
        #         dp[k] = 0
        #         return dp[k]
            
        #     if k == 1:
        #         dp[k] = 1
        #         return dp[k]

        #     if dp[k] is not None:
        #         return dp[k]

        #     power = 1
        #     while 2 ** (power + 1) <= k:
        #         power += 1
            
        #     bits = 1 + recurse(k - (2 ** power))
        #     dp[k] = bits
        #     return bits
        
        # ans = [recurse(i) for i in range(n+1)]
        # return ans

        dp = [0] * (n + 1)
        for i in range(1, n+1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp