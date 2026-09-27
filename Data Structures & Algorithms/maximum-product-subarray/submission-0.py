class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = -float('inf')
        min_product, max_product = 1, 1

        for num in nums:
            values = [num, num * min_product, num * max_product]
            min_product, max_product = min(values), max(values)

            ans = max(ans, *values)
        
        return ans
