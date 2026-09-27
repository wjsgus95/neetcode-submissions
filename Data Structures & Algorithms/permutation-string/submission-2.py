class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        S1, S2 = len(s1), len(s2)
        if S2 < S1:
            return False
            
        counter = Counter(s1)

        window_counter = Counter()
        for i in range(S1):
            window_counter[s2[i]] += 1
        
        left, right = 0, S1
        while right < S2:
            if window_counter == counter:
                return True
            
            window_counter[s2[left]] -= 1
            window_counter[s2[right]] += 1

            left += 1
            right += 1
        
        return window_counter == counter
        