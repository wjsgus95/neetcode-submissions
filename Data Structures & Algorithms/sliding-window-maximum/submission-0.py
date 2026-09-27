import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []

        for i in range(k - 1):
            heapq.heappush(heap, (-nums[i], i))
        
        ans = []
        
        for i in range(k - 1, len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            while len(heap) > k and heap[0][1] <= (i - k):
                heapq.heappop(heap)

            ans.append(-heap[0][0])
            
        return ans