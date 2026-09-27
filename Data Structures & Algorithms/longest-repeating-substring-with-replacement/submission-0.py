class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        S = len(s)
        counter = Counter()
        
        ans = 0

        max_count = 0
        left = 0

        for right in range(S):
            counter[s[right]] += 1
            max_count = max(max_count, counter[s[right]])

            while right - left + 1 - max_count > k:
                counter[s[left]] -= 1 
                left += 1
        
            ans = max(ans, right - left + 1)
    
        return ans