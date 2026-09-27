class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            stack.append(token)
            while stack[-1] in '*/+-':
                operand = stack.pop()

                right = stack.pop()
                left = stack.pop()

                left, right = int(left), int(right)
    
                if operand == '+':
                    result = left + right
                elif operand == '*':
                    result = left * right
                elif operand == '/':
                    result = int(left / right)
                else:
                    result = left - right
                
                stack.append(str(result))

        return int(stack[0])