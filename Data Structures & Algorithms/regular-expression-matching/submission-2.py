from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def preprocess() -> list[str]:
            t = []
            i = 0
            while i < len(p):
                if i == len(p) - 1 or p[i+1] != '*':
                    t.append(p[i])
                    i += 1
                else:
                    t.append(p[i:i+2])
                    i += 2
            return t

        p = preprocess()
        S, P = len(s), len(p)

        @lru_cache
        def recurse(x: int, y: int) -> bool:
            if x == S and y == P:
                return True
            
            if y == P:
                return False
            
            if x == S:
                return all(len(c) == 2 and c[1] == '*' for c in p[y:])

            matched = False
            if len(p[y]) == 2:
                if s[x] == p[y][0] or p[y][0] == '.':
                    matched = recurse(x + 1, y) or recurse(x + 1, y + 1)
                matched = matched or recurse(x, y + 1)
            elif p[y] == s[x] or p[y] =='.':
                matched = recurse(x + 1, y + 1)
            
            return matched
        
        return recurse(0, 0)
        