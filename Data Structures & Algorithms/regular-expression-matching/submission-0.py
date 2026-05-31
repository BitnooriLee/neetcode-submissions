class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n = len(s),len(p)
        dp = {}
        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if j >= n and i >= m: #out of bound -> found solution
                return True
            if j >= n :
                return False
            match = i< m and (s[i]==p[j] or p[j] == ".")
            if (j+1) < len(p) and p[j+1] == "*":
                return dfs(i, j+2) or (match and dfs(i+1,j)) 
            if match:
                return dfs(i+1, j+1)
            return False
        return dfs(0,0)