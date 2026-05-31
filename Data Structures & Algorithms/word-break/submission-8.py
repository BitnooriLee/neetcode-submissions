class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] *(n+1)
        maxlen = max((len(w) for w in wordDict), default=0)
        dp[0] = True
        wordset = set(wordDict)
        for i in range(n+1):
            if not dp[i]:
                continue
            #endLimit = min(n, i+maxlen)
            for j in range(i+1,i+1+maxlen):
                if j <= n and s[i:j] in wordset:
                    dp[j] = True
        return dp[n]


        