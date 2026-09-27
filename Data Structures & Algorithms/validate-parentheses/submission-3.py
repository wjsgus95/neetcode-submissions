class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            stack.append(c)

            if len(stack) >= 2:
                if stack[-1] == ')' and stack[-2] == '(':
                    stack.pop()
                    stack.pop()
                    continue
                if stack[-1] == ']' and stack[-2] == '[':
                    stack.pop()
                    stack.pop()
                    continue
                if stack[-1] == '}' and stack[-2] == '{':
                    stack.pop()
                    stack.pop()
                    continue

        return len(stack) == 0
 