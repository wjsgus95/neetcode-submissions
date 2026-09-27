import bisect
from collections import defaultdict

class TimeMap:
    def __init__(self):
        self.table = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.table[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.table[key]
        if not values:
            return ""
        
        left, right = 0, len(values) - 1
        ans = ""
        while left <= right:
            mid = (left + right) // 2
            t, v = values[mid]

            if t > timestamp:
                right = mid - 1
            elif t <= timestamp:
                ans = v
                left = mid + 1
        
        return ans
        
