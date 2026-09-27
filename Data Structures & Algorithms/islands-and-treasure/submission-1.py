from collections import deque
from typing import Iterator

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        X, Y = len(grid), len(grid[0])
        TREASURE = 0
        INF = 2 ** 31 - 1

        queue = deque()
        for x in range(X):
            for y in range(Y):
                if grid[x][y] == TREASURE:
                    queue.append((x, y, 0)) 
    
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        def adjacent_lands(x: int, y: int) -> Iterator[tuple[int, int]]:
            for i in range(4):
                nx = x + dx[i] 
                ny = y + dy[i]

                if 0 <= nx < X and 0 <= ny < Y:
                    if grid[nx][ny] > 0:
                        yield (nx, ny)

        while queue:
            x, y, dist = queue.popleft()
            for nx, ny in adjacent_lands(x, y):
                if grid[nx][ny] == INF:
                    grid[nx][ny] = dist + 1
                    queue.append((nx, ny, dist + 1))
        