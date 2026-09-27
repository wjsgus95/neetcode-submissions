class Solution:
    def countSubstrings(self, s: str) -> int:
        S = len(s)

        def odd_palindromes(mid: int) -> int:
            counts = 1
            left, right = mid - 1, mid + 1

            while 0 <= left and right < S:
                if s[left] == s[right]:
                    counts += 1
                else:
                    break
                
                left -= 1
                right += 1
            
            return counts
        
        def even_palindromes(left: int, right: int) -> int:
            counts = 0
            
            while 0 <= left and right < S:
                if s[left] == s[right]:
                    counts += 1
                else:
                    break
                
                left -= 1
                right += 1
            
            return counts
        
        ans = 0
        for i in range(S):
            ans += odd_palindromes(i)

            if i < S - 1:
                ans += even_palindromes(i, i+1)
        return ans


        