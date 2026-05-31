class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        maxlen = 0
        wordSet = set(wordDict)
        for word in wordDict:
            maxlen = max(maxlen, len(word))
            

        for i in range(n+1):
            if not dp[i]:
                continue
            for j in range(i+1,i+maxlen+1):
                if j <=n and s[i:j] in wordSet:
                    dp[j] = True
        return dp[n]