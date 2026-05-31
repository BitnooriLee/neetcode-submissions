class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        l = len(s)
        dp = [False]*(l+1)
        dp[0] = True
        wordset = set(wordDict)
        maxL = max((len(w) for w in wordset), default=0)
        for i in range(l+1):
            if not dp[i]:
                continue 
            endLimit = min(l, i+maxL)
            for j in range(i+1, endLimit+1):
                if s[i:j] in wordset:
                    dp[j] = True
        return dp[-1]

# O(n * m * k)
#n = len(s)
#m = len(wordDict)
#k = 평균 단어 길이

        