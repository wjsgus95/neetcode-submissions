class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        left_max = [0] * N
        right_max = [0] * N

        for i in range(1, N):
            left_max[i] = max(left_max[i-1], height[i-1])
        
        for i in range(N - 2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i+1])
        
        ans = 0
        for i in range(N):
            min_height = min(left_max[i], right_max[i])
            ans += max(min_height - height[i], 0)
        return ans
