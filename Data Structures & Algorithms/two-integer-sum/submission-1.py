class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = defaultdict(set)

        for i, num in enumerate(nums):
            values[num].add(i) 
        
        for num in values:
            if 2 * num == target:
                if len(values[num]) == 2:
                    return list(sorted(values[num]))
            elif target - num in values:
                a = list(values[num])
                b = list(values[target - num])

                return list(sorted(a + b))
