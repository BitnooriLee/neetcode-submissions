class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m,n = len(s), len(t)
        if m < n :
            return 0

        dp = [0] * (n+1)
        dp[0]= 1
        for ch in s:
            for i in range(n,0,-1):
                if ch == t[i-1]:
                    dp[i] += dp[i-1]

        return dp[n]