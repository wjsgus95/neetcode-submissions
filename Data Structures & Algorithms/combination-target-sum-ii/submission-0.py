class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        counter = Counter(candidates)
        numbers = list(tuple(counter.items()))

        ans = []
        accumulated = 0
        stack = []
        def backtrack(index: int) -> None:
            nonlocal accumulated

            if accumulated > target:
                return
            elif accumulated == target:
                combination = []
                for v, c in stack:
                    combination += [v] * c
                ans.append(combination)
                return

            if index == len(numbers):
                return
           
            value, count = numbers[index]
            for i in range(count + 1):
                stack.append((value, i))
                accumulated += value * i

                backtrack(index + 1)

                stack.pop()
                accumulated -= value * i
        
        backtrack(0)
        return ans