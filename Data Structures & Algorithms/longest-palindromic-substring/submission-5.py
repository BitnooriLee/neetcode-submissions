class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s 
        dp = [False]*n    
        bestl, bestr = 0,0 
        for i in range(n-1,-1,-1):
            prev = False # dp[i+1][j-1]
            for j in range(i, n):
                tmp = dp[j] 
                if s[i] == s[j] and (j-i <2 or prev):
                    dp[j] = True
                    if j-i > bestr- bestl:
                        bestl, bestr = i,j

                else:
                    dp[j] = False
                prev = tmp 

        return s[bestl:bestr+1]

        