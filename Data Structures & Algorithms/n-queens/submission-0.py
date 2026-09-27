from collections import defaultdict

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
    
        queens = [] # y values

        cols = defaultdict(bool) # y
        left = defaultdict(bool) # x - y
        right = defaultdict(bool) # x + y

        def eligible(x: int, y: int) -> bool:
            taken = cols[y] or left[x - y] or right[x + y]
            return not taken

        def capture() -> list[str]:
            board = []

            for x in range(n):
                board.append([])
                for y in range(n):
                    if queens[x] == y:
                        board[x].append('Q')
                    else:
                        board[x].append('.')
            
            transformed = []
            for row in board:
                transformed.append(''.join(row))
            return transformed

        def backtrack(x: int) -> None:
            if len(queens) == n:
                ans.append(capture()) 
            
            for y in range(n):
                if eligible(x, y):
                    cols[y] = True
                    left[x - y] = True
                    right[x + y] = True

                    queens.append(y)
                    backtrack(x + 1)
                    queens.pop()

                    cols[y] = False
                    left[x - y] = False
                    right[x + y] = False

        backtrack(0)
        return ans