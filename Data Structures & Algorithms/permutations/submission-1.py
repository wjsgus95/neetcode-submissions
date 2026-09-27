class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        visited = set()
        path = []

        def recurse():
            if len(nums) == len(path):
                ans.append(path[:])
                return

            for i in range(len(nums)):
                if i not in visited:
                    visited.add(i)
                    path.append(nums[i])

                    recurse()

                    visited.remove(i)
                    path.pop()
        
        recurse()
        return ans