from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        X, Y = len(heights), len(heights[0])

        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]
        def neighbors(x: int, y: int) -> Iterator[tuple[int, int]]:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < X and 0 <= ny < Y:
                    yield nx, ny

        def flow(queue: deque) -> set[tuple[int, int]]:
            flowable = set(queue)

            while queue:
                x, y = queue.popleft()

                for nx, ny in neighbors(x, y):
                    if (nx, ny) not in flowable:
                        if heights[nx][ny] >= heights[x][y]:
                            flowable.add((nx, ny))
                            queue.append((nx, ny))
            
            return flowable
        
        pacific_queue = deque()
        for y in range(1, Y):
            pacific_queue.append((0, y))
        for x in range(X):
            pacific_queue.append((x, 0))
        pacific_flow = flow(pacific_queue) 

        atlantic_queue = deque()
        for y in range(Y - 1):
            atlantic_queue.append((X - 1, y))
        for x in range(X):
            atlantic_queue.append((x, Y - 1))
        atlantic_flow = flow(atlantic_queue)

        ans = []
        for x in range(X):
            for y in range(Y):
                if (x, y) in pacific_flow and (x, y) in atlantic_flow:
                    ans.append([x, y])
        print(pacific_flow)
        print(atlantic_flow)
        return ans

        

        