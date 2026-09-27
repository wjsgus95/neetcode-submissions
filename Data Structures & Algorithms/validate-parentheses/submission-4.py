class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            stack.append(c)

            if len(stack) >= 2:
                if stack[-1] == ')' and stack[-2] == '(':
                    stack.pop()
                    stack.pop()
                elif stack[-1] == ']' and stack[-2] == '[':
                    stack.pop()
                    stack.pop()
                elif stack[-1] == '}' and stack[-2] == '{':
                    stack.pop()
                    stack.pop()

        return len(stack) == 0
 