from itertools import pairwise
from collections import deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        ans = []

        graph = dict()
        influx = defaultdict(int)

        for word in words:
            for c in word:
                if c not in graph:
                    graph[c] = set()

        for prev, curr in pairwise(words):
            i = 0

            exists_diff = False
            while i < len(prev) and i < len(curr):
                if prev[i] != curr[i]:
                    exists_diff = True
                    if curr[i] not in graph[prev[i]]:
                        graph[prev[i]].add(curr[i])
                        influx[curr[i]] += 1
                    break
                i += 1
            
            if not exists_diff and len(prev) > len(curr):
                return ""

        queue = deque()
        for c in graph:
            if influx[c] == 0:
                queue.append(c)
        
        while queue:
            c = queue.popleft()
            ans.append(c)

            for dst in graph[c]:
                influx[dst] -= 1
                if influx[dst] == 0:
                    queue.append(dst)

        if len(ans) != len(graph):
            return ""
        
        return ''.join(ans)