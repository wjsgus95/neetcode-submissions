class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        dp = [False] * N
        dp[0] = True

        def recurse(index: int):
            jumps = nums[index] 
            for i in range(index + 1, index + 1 + jumps):
                if i < N and not dp[i]:
                    dp[i] = True
                    recurse(i)
        
        recurse(0)
        return dp[-1]