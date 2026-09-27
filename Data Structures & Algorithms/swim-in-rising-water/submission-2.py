import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        heap = []

        visited = [[float('inf')] * N for _ in range(N)]
        visited[0][0] = grid[0][0]
        heap.append((grid[0][0], 0, 0))

        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        def neighbors(x: int, y: int):
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < N and 0 <= ny < N:
                    yield nx, ny

        while heap:
            accu, x, y = heapq.heappop(heap)
            if x == N - 1 and y == N - 1:
                return accu

            for nx, ny in neighbors(x, y):
                new_accu = max(accu, grid[nx][ny])
                if visited[nx][ny] > new_accu:
                    visited[nx][ny] = new_accu
                    heapq.heappush(heap, (new_accu, nx, ny))