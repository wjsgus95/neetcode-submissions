class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [[None] * N for _ in range(N)]

        def recurse(begin: int, end: int) -> int:
            if begin > end:
                return 0
            
            if dp[begin][end] is not None:
                return dp[begin][end]

            max_score = 0
            for reserve in range(begin, end + 1):
                score = recurse(begin, reserve - 1) + recurse(reserve + 1, end)

                left = 1 if begin == 0 else nums[begin-1]
                right = 1 if end == N - 1 else nums[end+1]

                score += left * right * nums[reserve]

                max_score = max(score, max_score)
            
            dp[begin][end] = max_score
            return max_score
        
        return recurse(0, N-1)