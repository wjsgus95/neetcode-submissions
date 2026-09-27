class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(sorted(zip(position, speed)))
        N = len(cars)

        stack = []

        for i in range(N - 1, -1, -1):
            pos, speed = cars[i]
            stack.append((target - pos) / speed)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
