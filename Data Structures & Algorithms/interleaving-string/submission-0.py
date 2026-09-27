class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        S1, S2, S3 = len(s1), len(s2), len(s3)
        if S1 + S2 != S3:
            return False
            
        dp = [[None] * (S2 + 1) for _ in range(S1 + 1)]

        def interleave(index1: int, index2: int) -> bool:
            if index1 == S1 and index2 == S2:
                return True

            if dp[index1][index2] is not None:
                return dp[index1][index2]

            index3 = index1 + index2
            if index3 == S3:
                return False

            ans1 = False
            if index1 < S1 and s3[index3] == s1[index1]:
                ans1 = interleave(index1+1, index2)
            
            ans2 = False
            if index2 < S2 and s3[index3] == s2[index2]:
                ans2 = interleave(index1, index2+1)
            
            dp[index1][index2] = ans1 or ans2
            return dp[index1][index2]
        
        return interleave(0, 0)