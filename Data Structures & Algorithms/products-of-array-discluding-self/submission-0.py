class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        left = [0] * N
        right = [0] * N

        left[0] = nums[0]
        right[-1] = nums[-1]

        for i in range(1, N):
            left[i] = left[i-1] * nums[i]
        for i in range(N - 2, -1, -1):
            right[i] = right[i+1] * nums[i]
        
        ans = []
        for i in range(N):
            if i == 0:
                ans.append(right[1])
            elif i == N - 1:
                ans.append(left[N-2])
            else:
                ans.append(left[i-1] * right[i+1])
        return ans