from collections import deque

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        queue = deque() 

        visited = [[float('inf')] * N for _ in range(N)]
        visited[0][0] = grid[0][0]
        queue.append((0, 0, grid[0][0]))

        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        def neighbors(x: int, y: int):
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < N and 0 <= ny < N:
                    yield nx, ny

        ans = float('inf')
        while queue:
            x, y, accu = queue.popleft()
            if x == N - 1 and y == N - 1:
                ans = min(ans, accu)

            for nx, ny in neighbors(x, y):
                new_accu = max(accu, grid[nx][ny])
                if visited[nx][ny] > new_accu:
                    visited[nx][ny] = new_accu
                    queue.append((nx, ny, new_accu))
        
        return ans