from collections import Counter

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counter = Counter(nums)

        ans = 0
        for num in nums:
            if counter[num-1] == 0:
                sequence = 0
                index = num
                while counter[index] > 0:
                    sequence += 1
                    index += 1
                ans = max(sequence, ans)
        
        return ans
                
        
