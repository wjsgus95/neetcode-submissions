class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        S = len(s)
        dp = [None] * (S + 1)

        def match(base: int, target: str) -> bool:
            return s[base: base+len(target)] == target

        def recurse(index: int) -> bool:
            if dp[index] is not None:
                return dp[index]
            
            if index == S:
                dp[S] = True
                return dp[S]

            matched = False
            for word in wordDict:
                if match(index, word):
                    matched = matched or recurse(index + len(word))
            
            dp[index] = matched
            return dp[index]
        
        return recurse(0)