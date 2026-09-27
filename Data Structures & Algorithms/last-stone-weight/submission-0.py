import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            first = -first
            second = -second

            if first != second:
                new_stone = first - second
                heapq.heappush(stones, -new_stone)
                
        return -stones[0] if stones else 0