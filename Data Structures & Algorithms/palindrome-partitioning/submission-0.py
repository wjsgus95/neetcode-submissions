class Solution:
    def partition(self, s: str) -> List[List[str]]:
        S = len(s)
        ans = []

        dp = [[False] * S for _ in range(S)]
        for mid in range(S):
            dp[mid][mid] = True
            left, right = mid - 1, mid + 1
            while 0 <= left and right < S:
                if s[left] == s[right]:
                    dp[left][right] = True
                else:
                    break
                
                left -= 1
                right += 1
        
        for left in range(S - 1):
            right = left + 1
            while 0 <= left and right < S:
                if s[left] == s[right]:
                    dp[left][right] = True
                else:
                    break
                
                left -= 1
                right += 1

        stack = []
        def backtrack(begin: int) -> None:
            if begin == S:
                ans.append(list(stack))
                return
            
            for i in range(begin, S):
                if dp[begin][i]:
                    stack.append(s[begin:i+1])
                    backtrack(i + 1)
                    stack.pop()
        
        backtrack(0)
        return ans
            
