class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)

        for index, temperature in enumerate(temperatures):
            while stack and stack[-1][1] < temperature:
                prev_index, _ = stack.pop()
                ans[prev_index] = index - prev_index
            
            stack.append((index, temperature))
        
        return ans
        