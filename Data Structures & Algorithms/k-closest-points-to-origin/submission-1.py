class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            value = -(x ** 2 + y ** 2)
            heapq.heappush(heap, (value, x, y))

            if len(heap) > k:
                heapq.heappop(heap)

        ans = []
        for _ in range(k):
            _, x, y = heapq.heappop(heap)
            ans.append([x, y])
        
        return ans