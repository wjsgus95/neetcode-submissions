class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        N = len(nums)

        dp = [[None] * N for _ in range(N)]

        def recurse(i: int, j: int) -> int:
            if j - i < 2:
                return 0
            
            if dp[i][j] is not None:
                return dp[i][j]

            max_value = 0
            for k in range(i + 1, j):
                value = recurse(i, k) + recurse(k, j) + nums[i] * nums[k] * nums[j]
                max_value = max(value, max_value)
            dp[i][j] = max_value 
            return dp[i][j]
        
        return recurse(0, len(nums) - 1)

        