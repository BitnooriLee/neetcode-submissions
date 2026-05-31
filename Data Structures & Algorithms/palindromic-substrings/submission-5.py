class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1

        dp = [False]*n
        cnt = 0 

        for i in range(n-1,-1,-1):
            prev = False
            for j in range(i,n):
                tmp = dp[j] 
                if s[i] == s[j] and (j-i <2 or prev):
                    dp[j] = True
                    cnt+= 1
                else:
                    dp[j] = False
                prev = tmp

        return cnt

