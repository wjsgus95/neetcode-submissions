from collections import Counter

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        summations = Counter()
        N = len(nums)
        for num in nums:
            if len(summations) == 0:
                summations[num] += 1
                summations[-num] += 1
            else:
                counter = Counter()
                for s in summations:
                    counter[s + num] += summations[s]
                    counter[s - num] += summations[s]
                summations = counter
        
        return summations[target]