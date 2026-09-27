class Solution:
    def checkValidString(self, s: str) -> bool:
        lefts = []
        stars = []

        for i, c in enumerate(s):
            if c == '(':
                lefts.append(i)
            elif c == '*':
                stars.append(i)
            elif c == ')':
                if lefts:
                    lefts.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
        
        while lefts and stars:
            if lefts.pop() > stars.pop():
                return False
        
        return not lefts