class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        l = len(s)
        dp = [False] * (l+1)
        dp[0] = True
        max_len = 0 
        wordSet = set()
        for word in wordDict:
            max_len = max(max_len, len(word))
            wordSet.add(word)

        for i in range(l+1):
            if not dp[i]:
                continue
            for j in range(i+1, i+max_len+1): # j 포함 안됨, dp[j]는 s[j-1]까지 본것 
                if j <= l and s[i:j] in wordSet:
                    dp[j] = True

        return dp[l]
                
                        