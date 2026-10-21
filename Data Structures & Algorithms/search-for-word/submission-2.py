class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        X, Y = len(board), len(board[0])
        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]

        path = []
        def backtrack(x: int, y: int) -> bool:
            path.append((x, y))

            index = len(path) - 1
            if board[x][y] != word[index]:
                path.pop()
                return False
            
            if len(word) == len(path):
                path.pop()
                return True
            
            found = False
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < X and 0 <= ny < Y:
                    if (nx, ny) not in path:
                        found = found or backtrack(nx, ny)
            
            path.pop()
            return found

            
        for x in range(X):
            for y in range(Y):
                if backtrack(x, y):
                    return True
        
        return False