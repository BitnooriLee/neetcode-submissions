class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(s) == 1 and len(p) == 1:
            if p == s or p == "*":
                return True
            else:
                return False
        
        m,n = len(s), len(p)

        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[0][0] = True

        for j in range(1,n+1):
            if p[j-1] == "*":
                dp[0][j] = dp[0][j-2] # "", "a*" True 

        def match(i,j):
            if s[i-1] == p[j-1] or (p[j-1] == '.'):
                return True
            else: return False 


        for i in range(1,m+1):
            for j in range(1,n+1):
                if not p[j-1] == "*":
                    if match(i,j):
                        dp[i][j] = dp[i-1][j-1]

                else:
                    dp[i][j] = dp[i][j-2] # 사용 x 
                    if match(i,j-1):
                        dp[i][j] = dp[i][j] or dp[i-1][j] # aaa a* 가 true이려면 맨앞의 *앞이 a로 같아야 함 


        return dp[m][n]
                

            
        