class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        stack = []
        accumulated = 0

        def backtrack(index: int) -> None:
            nonlocal accumulated

            if index == len(nums):
                return
                
            if accumulated > target:
                return
            
            if accumulated == target:
                ans.append(list(stack))
                return

            for i in range(index, len(nums)):
                if nums[i] + accumulated > target:
                    break

                stack.append(nums[i])
                accumulated += nums[i]

                backtrack(i)

                stack.pop()
                accumulated -= nums[i]

        nums.sort()
        backtrack(0)

        return ans