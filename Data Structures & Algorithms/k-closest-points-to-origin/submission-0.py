class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            heapq.heappush(heap, (x ** 2 + y ** 2, x, y))

        ans = []
        for _ in range(k):
            _, x, y = heapq.heappop(heap)
            ans.append([x, y])
        
        return ans