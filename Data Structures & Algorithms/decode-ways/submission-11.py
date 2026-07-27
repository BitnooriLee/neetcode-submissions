class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l = len(s)
        dp = [0] * (l+1)
        dp[0] = 1
        for i in range(1,l+1):
            if i > 1 and 10<= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
            if s[i-1] != "0":
                dp[i] += dp[i-1]

        return dp[l]