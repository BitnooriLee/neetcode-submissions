class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        if n == 1:
            if s[0] in wordDict: return True 
            else: return False

        dp = [False] * (n+1)
        dp[0] = True

        for i in range(0,n+1):
            for word in wordDict:
                l = len(word)
                print(s[i:i+l], word)
                if dp[i] and i+l <= n and s[i:i+l] == word:
                    
                    dp[i+l] = True
        print(dp)
        return dp[n]


        