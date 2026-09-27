class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        M, N = len(word1), len(word2)
        if M == 0 or N == 0:
            return max(M, N)

        dp = [[-1] * (N+1) for _ in range(M+1)]

        def rectify(left: int, right: int) -> int:
            if dp[left][right] >= 0:
                return dp[left][right]

            if left == M:
                value = (N - right)
                dp[left][right] = value
                return value
            
            if right == N:
                value = (M - left)
                dp[left][right] = value
                return value
            
            if word1[left] == word2[right]:
                return rectify(left + 1, right + 1)
            else:
                insert = rectify(left, right + 1)
                delete = rectify(left + 1, right)
                replace = rectify(left + 1, right + 1)

                value = min(insert + 1, delete + 1, replace + 1)
                dp[left][right] = value
                return value
        
        return rectify(0, 0)
        
