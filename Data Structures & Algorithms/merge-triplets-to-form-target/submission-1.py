class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ans = [-float('inf'), -float('inf'), -float('inf')]

        target_a, target_b, target_c = target
        for a, b, c in triplets:
            if a <= target_a and b <= target_b and c <= target_c:
                ans = [max(a, ans[0]), max(b, ans[1]), max(c, ans[2])]

        return ans == target