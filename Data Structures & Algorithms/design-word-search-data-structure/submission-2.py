class TrieNode:
    def __init__(self):
        self.terminal = False
        self.children = dict()
    
    def add(self, word: str) -> None:
        node = self

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            
            node = node.children[c]
        
        node.terminal = True
        
    def search(self, word: str) -> bool:
        queue = deque()
        queue.append((self, 0))

        while queue:
            node, index = queue.popleft()

            if index == len(word):
                if node.terminal:
                    return True

                continue
            
            token = word[index]
            if token == '.':
                for child in node.children.values():
                    queue.append((child, index + 1))
            elif token in node.children:
                queue.append((node.children[token], index + 1))
        
        return False
        
    
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        self.root.add(word)

    def search(self, word: str) -> bool:
        return self.root.search(word)
