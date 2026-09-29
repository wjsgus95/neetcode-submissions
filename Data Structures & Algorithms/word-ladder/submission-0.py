from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        visited = dict()
        for word in wordList:
            visited[word] = 10 ** 10

        def is_one_off(word1: str, word2: str) -> bool:
            diff = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    diff += 1
                
                if diff > 1:
                    return False
            
            return diff == 1
        
        graph = defaultdict(set)
        for word1 in wordList:
            for word2 in wordList:
                if is_one_off(word1, word2):
                    graph[word1].add(word2)
                    graph[word2].add(word1)
        
            if is_one_off(beginWord, word1):
                graph[beginWord].add(word1)
            
        queue = deque()
        queue.append((beginWord, 1))
        while queue:
            word, distance = queue.popleft()

            for nextWord in graph[word]:
                if visited[nextWord] > distance + 1:
                    visited[nextWord] = distance + 1
                    queue.append((nextWord, distance + 1))
        
        return visited[endWord] if visited[endWord] < 10 ** 10 else 0