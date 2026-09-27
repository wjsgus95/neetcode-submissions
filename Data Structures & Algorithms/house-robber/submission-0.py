class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [None] * N

        def recurse(index: int) -> int:
            if index >= N:
                return 0

            if dp[index] is not None:
                return dp[index]
            
            value = max(recurse(index + 1), nums[index] + recurse(index + 2))
            dp[index] = value
            return value
        
        return recurse(0)