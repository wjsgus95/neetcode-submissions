class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        S1, S2 = len(text1), len(text2)
        dp = [[None] * (S2 + 1) for _ in range(S1 + 1)]

        def backtrack(index1: int, index2: int) -> int:
            if dp[index1][index2] is not None:
                return dp[index1][index2]

            if index1 == S1 or index2 == S2:
                return 0
            
            child1 = 0
            if text1[index1] == text2[index2]:
                child1 = backtrack(index1 + 1, index2 + 1) + 1
            
            child2 = backtrack(index1 + 1, index2)
            child3 = backtrack(index1, index2 + 1)

            dp[index1][index2] = max(child1, child2, child3)
            return dp[index1][index2]
        
        return backtrack(0, 0)

        