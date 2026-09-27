class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums) 
        numbers = list(tuple(i) for i in counter.items())

        ans = []
        stack = []
        def backtrack(index: int) -> None:
            if index == len(numbers):
                subset = []
                for v, c in stack: 
                    for _ in range(c):
                        subset.append(v)
                ans.append(subset)
                return
            
            value, count = numbers[index]
            for c in range(count + 1):
                stack.append((value, c))
                backtrack(index + 1)
                stack.pop()
        
        backtrack(0)
        return ans