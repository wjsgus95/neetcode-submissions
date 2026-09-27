class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        dp = [None] * (N + 1)

        def recurse(index: int) -> int:
            if dp[index] is not None:
                return dp[index]
            
            if index == 0 or index == 1:
                return 0
            
            value1 = recurse(index - 1) + cost[index - 1]
            value2 = recurse(index - 2) + cost[index - 2]
            dp[index] = min(value1, value2)
            return dp[index]
        
        return recurse(N)
