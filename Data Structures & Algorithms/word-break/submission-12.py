class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordSet = set()
        l = len(s)
        dp = [False] * (len(s)+1)
        dp[0] = True
        max_len = 0
        for word in wordDict:
            max_len = max(max_len, len(word))
            wordSet.add(word)
            
        for i in range(len(s)):
            if not dp[i]:
                continue
            for j in range(i+1, i+max_len+1):
                if j <= l and s[i:j] in wordSet:
                    dp[j] = True
        return dp[l]

        