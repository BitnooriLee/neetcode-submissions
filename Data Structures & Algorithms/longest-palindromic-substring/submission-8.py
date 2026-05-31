class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [False] * (len(s))
        if len(s) <= 1:
            return s 
        bestl, bestr = 0,0 

        for i in range(len(s)-1,-1,-1):
            prev = False
            for j in range(i,len(s)):
                tmp = dp[j]
                if (s[i] == s[j]) and (j - i < 2 or prev):
                    dp[j] = True
                    if j-i > bestr - bestl:
                        bestr, bestl = j,i
                else:
                    dp[j] = False
                prev = tmp

        return s[bestl:bestr+1]