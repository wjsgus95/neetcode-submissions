from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        X, Y = len(grid), len(grid[0])

        def fresh_neighbors(x: int, y: int):
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < X and 0 <= ny < Y and grid[nx][ny] == 1:
                    yield nx, ny

        def cycle() -> bool:
            frontier = set()

            for x in range(X):
                for y in range(Y):
                    if grid[x][y] == 2:
                        for nx, ny in fresh_neighbors(x, y):
                            frontier.add((nx, ny))

            for x, y in frontier:
                grid[x][y] = 2
            
            return len(frontier) == 0
        
        ans = 0
        while not cycle():
            ans += 1
        
        for x in range(X):
            for y in range(Y):
                if grid[x][y] == 1:
                    return -1
    
        return ans


