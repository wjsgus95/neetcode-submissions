import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def get_cost(k: int) -> int:
            result = 0 

            for p in piles:
                result += math.ceil(p / k)
            
            return result
        
        left, right = 1, max(piles)
        while left <= right:
            mid = (left + right) // 2
            cost = get_cost(mid)

            if cost > h:
                left = mid + 1
            elif cost <= h:
                right = mid - 1
                ans = mid
            
        return ans