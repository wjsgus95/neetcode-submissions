class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        ans = 0

        prev_frontier = 0
        frontier = nums[0]

        while prev_frontier < N - 1:
            tmp = frontier
            for i in range(prev_frontier + 1, min(N, frontier + 1)):
                frontier = max(frontier, nums[i] + i)
            prev_frontier = tmp
            ans += 1
        
        return ans