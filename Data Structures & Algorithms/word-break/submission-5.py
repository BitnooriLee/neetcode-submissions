class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        l = len(s)
        dp = [False]*(l+1)
        dp[0] = True

        for i in range(l+1):
            for w in wordDict:
                length = len(w)
                if dp[i] and i+length <= l and s[i:i+length] == w:
                    dp[i+length] = True 
        return dp[-1]
        