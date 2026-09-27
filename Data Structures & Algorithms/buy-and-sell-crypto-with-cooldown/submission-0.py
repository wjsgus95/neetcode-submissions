class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        FREE = 0
        HOLD = 1

        N = len(prices)
        dp = [[None] * 2 for _ in range(N)]

        def recurse(index: int, state: int) -> int:
            if index >= N:
                return 0
            
            if dp[index][state] is not None:
                return dp[index][state]

            if state == FREE:
                buy = -prices[index] + recurse(index + 1, HOLD)
                skip = recurse(index + 1, FREE)

                dp[index][state] = max(buy, skip)
            
            if state == HOLD:
                sell = prices[index] + recurse(index + 2, FREE)
                hold = recurse(index + 1, HOLD)

                dp[index][state] = max(sell, hold)
            
            return dp[index][state]
        
        return recurse(0, FREE)
            