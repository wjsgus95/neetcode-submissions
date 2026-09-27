class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        ans = []
        def recurse(index: int, subset: list = []) -> None:
            if index == N:
                ans.append(subset)
                return
            
            subset1 = list(subset)
            subset2 = list(subset)

            recurse(index + 1, subset1)

            subset2.append(nums[index])
            recurse(index + 1, subset2)
        
        recurse(0)
        return ans
        