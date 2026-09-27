from collections import Counter, defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)

        counter = Counter()
        for num in nums:
            counter[num] += 1
        
        inverted = defaultdict(list)
        for num in counter:
            count = counter[num]
            inverted[count].append(num)
        
        ans = []
        for i in range(N, -1, -1):
            if inverted[i]:
                numbers = inverted[i]
                for n in numbers:
                    ans.append(n)
                    if len(ans) == k:
                        return ans
            
