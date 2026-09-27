from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        X, Y = len(grid), len(grid[0])
        visited = [[False] * Y for _ in range(X)]

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        def search(x: int, y: int) -> int:
            if visited[x][y]:
                return 0

            if grid[x][y] == 0:
                return 0
            
            queue = deque()
            queue.append((x, y))
            visited[x][y] = True

            area = 0
            while queue:
                x, y = queue.popleft()
                area += 1

                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]

                    if 0 <= nx < X and 0 <= ny < Y:
                        if grid[nx][ny] == 1 and not visited[nx][ny]:
                            queue.append((nx, ny))
                            visited[nx][ny] = True
            
            return area
        
        for x in range(X):
            for y in range(Y):
                ans = max(ans, search(x, y))
        return ans
