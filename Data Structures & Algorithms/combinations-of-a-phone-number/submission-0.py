class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        N = len(digits)
        if N == 0:
            return []

        table = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        letters = []
        def backtrack(index: int) -> None:
            if index == N:
                ans.append(''.join(letters))
                return
            
            for c in table[digits[index]]:
                letters.append(c)
                backtrack(index + 1)
                letters.pop()
            
        backtrack(0)
        return ans
        