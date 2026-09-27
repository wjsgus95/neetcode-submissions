class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        stack = []

        num_open = 0
        num_close = 0

        def backtrack() -> None:
            nonlocal num_open, num_close

            if len(stack) == n * 2:
                if num_open == n and num_close == n:
                    ans.append(''.join(stack))             
                return
            
            if num_open < n:
                stack.append('(')
                num_open += 1

                backtrack()

                stack.pop()
                num_open -= 1
            
            if num_close < num_open:
                stack.append(')')
                num_close += 1

                backtrack()

                stack.pop()
                num_close -= 1
            
        backtrack()
        return ans
        