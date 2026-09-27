class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        visited = set()
        numbers = []

        def recurse(index: int) -> None:
            if len(numbers) == len(nums) - 1:
                ans.append(numbers + [nums[index]])
                return

            visited.add(index)
            numbers.append(nums[index])

            for i in range(len(nums)):
                if i in visited:
                    continue
                
                recurse(i)
        
            visited.remove(index)
            numbers.pop()
        
        for i in range(len(nums)):
            recurse(i)
        
        return ans