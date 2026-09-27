class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [[None] * N for _ in range(N)]

        def backtrack(prev: int, curr: int) -> int:
            if curr == N:
                return 0
            
            if dp[prev][curr] is not None:
                return dp[prev][curr]
            
            result = 0

            # continue the subsequence if applicable
            if prev == -1 or nums[curr] > nums[prev]:
                result = max(result, backtrack(curr, curr + 1) + 1)

            # skip current element
            result = max(result, backtrack(prev, curr + 1))

            dp[prev][curr] = result
            return result
        
        return backtrack(-1, 0)


