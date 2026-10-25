class TrieNode:
    def __init__(self):
        self.children = dict()
        self.terminal = False
        
    def add(self, word: str):
        node = self

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            
            node = node.children[c]

        node.terminal = True
    
    def advance(self, char: str) -> Optional[TrieNode]:
        if char in self.children:
            return self.children[char]

        return None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        X, Y = len(board), len(board[0])
        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]

        found = set()

        trie = TrieNode()
        for word in words:
            trie.add(word)

        visited = set()
        path = []
        def backtrack(x: int, y: int, node: TrieNode) -> None:
            if (x, y) in visited:
                return

            node = node.advance(board[x][y])
            if not node:
                return

            visited.add((x, y))
            path.append(board[x][y])

            if node.terminal:
                word = ''.join(path)
                found.add(word)
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < X and 0 <= ny < Y:
                    backtrack(nx, ny, node)
            
            visited.remove((x, y))
            path.pop()
        
        for x in range(X):
            for y in range(Y):
                backtrack(x, y, trie)
        
        return list(found)


        