class Solution:
    def solve(self, board: List[List[str]]) -> None:
        X, Y = len(board), len(board[0])
        visited = [[False] * Y for _ in range(X)]

        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]

        def surrounded(x: int, y: int) -> bool:
            if visited[x][y]:
                return False
            
            if board[x][y] == 'X':
                return False

            result = True
            queue = deque()            
            queue.append((x, y))

            while queue:
                x, y = queue.popleft()

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0 <= nx < X and 0 <= ny < Y:
                        if not visited[nx][ny] and board[nx][ny] == 'O':
                            visited[nx][ny] = True
                            queue.append((nx, ny))
                    else:
                        result = False
            
            return result
        
        def fill(x: int, y: int) -> None:
            queue = deque()
            queue.append((x, y))

            while queue:
                x, y = queue.popleft()
                board[x][y] = 'X'

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0 <= nx < X and 0 <= ny < Y:
                        if board[nx][ny] == 'O':
                            queue.append((nx, ny))

        for x in range(X):
            for y in range(Y):
                if surrounded(x, y):
                    fill(x, y)
        