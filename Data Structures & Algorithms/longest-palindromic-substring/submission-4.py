class Solution:
    def longestPalindrome(self, s: str) -> str:
        S = len(s)
        if S == 1:
            return s
        ans = s[0]
        
        for mid in range(1, S):
            left, right = mid, mid
            while 0 <= left and right < S:
                if s[left] == s[right]:
                    left -= 1
                    right += 1
                else:
                    break
            
            left += 1
            right -= 1
            substr = s[left:right+1]
            ans = substr if len(substr) > len(ans) else ans

            left, right = mid - 1, mid
            if s[left] != s[right]:
                continue

            while 0 <= left and right < S:
                if s[left] == s[right]:
                    left -= 1
                    right += 1
                else:
                    break
            
            left += 1
            right -= 1
            substr = s[left:right+1]
            ans = substr if len(substr) > len(ans) else ans

        return ans