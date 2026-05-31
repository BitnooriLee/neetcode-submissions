class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        residx, resLen = 0,0
        dp = [[False]*n for _ in range(n)]

        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i]==s[j] and (j-i <=2 or dp[i+1][j-1]): # 2보다 작으면 항상 트루 
                    dp[i][j] = True
                    if resLen < (j-i+1):
                        residx = i
                        resLen = j-i+1

        return s[residx:residx+resLen]

        