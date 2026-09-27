class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        stack = []
        accumulated = 0

        def backtrack(index: int) -> None:
            nonlocal accumulated

            if index == len(nums):
                return
                
            if accumulated + nums[index] > target:
                return
            
            if accumulated + nums[index] == target:
                print(accumulated, nums[index], target)
                ans.append(list(stack + [nums[index]]))
                return

            stack.append(nums[index])
            accumulated += nums[index]

            for i in range(index, len(nums)):
                backtrack(i)

            stack.pop()
            accumulated -= nums[index]

        nums.sort()
        for i in range(len(nums)):
            backtrack(i)

        return ans