class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s) 
        if n <=1:
            return s
        bestl, bestr = 0,0
        dp = [False]*len(s)
        for i in range(n-1,-1,-1):
            prev = False
            for j in range(i,n):
                tmp = dp[j]
                if s[i] == s[j] and (j-i < 2 or prev):
                    dp[j] = True
                    if j-i > bestr-bestl:
                        bestr,bestl = j,i
                else:
                    dp[j] = False
                prev = tmp
        
        return s[bestl:bestr+1]
        