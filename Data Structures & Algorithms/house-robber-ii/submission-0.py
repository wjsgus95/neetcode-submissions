class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)

        dp = [[None, None] for _ in range(N+1)]
        def traverse(index: int, flag: bool) -> int:
            if index >= N:
                return 0
            
            i = 1 if flag else 0
            if dp[index][i] is not None:
                return dp[index][i]

            if index == 0:
                value1 = nums[index] + traverse(index + 2, True)
            else:
                value1 = nums[index] + traverse(index + 2, flag)
            value2 = traverse(index+1, flag)

            if index == N - 1 and flag:
                return 0

            value = max(value1, value2)

            dp[index][i] = value
            return value
        
        return traverse(0, False)
        