class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        accumulated = nums[0]
        for i in range(1, len(nums)):
            if accumulated < 0:
                accumulated = nums[i]
            else:
                accumulated += nums[i]
            
            ans = max(ans, accumulated)
        
        return ans

        