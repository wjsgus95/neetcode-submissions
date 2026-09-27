import bisect

from collections import defaultdict, Counter

class CountSquares:
    def __init__(self):
        self.counters = defaultdict(Counter)

    def add(self, point: List[int]) -> None:
        x, y = point

        self.counters[x][y] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        ans = 0

        for ny in self.counters[x]:
            length = ny - y

            if length == 0:
                continue
            
            nx = x - length
            ans += self.counters[x][ny] * self.counters[nx][y] * self.counters[nx][ny]

            nx = x + length
            ans += self.counters[x][ny] * self.counters[nx][y] * self.counters[nx][ny]

        return ans