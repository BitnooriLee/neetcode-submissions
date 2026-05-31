class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1), len(word2)
        dp = {} # key: (i,j), value distance
        def dfs(i,j):
            if i == m:
                return n - j # remove remaining of word2 
            if j == n :
                return m - i 
            if (i,j) in dp:
                return dp[(i,j)]
            if word1[i] == word2[j]:# no add 
                dp[(i,j)] = dfs(i+1, j+1) 
            else: # add distance 1 
                res = min(dfs(i+1, j), dfs(i,j+1)) 
                res = min(res, dfs(i+1, j+1)) 
                dp[(i,j)] = res + 1 
            return dp[(i,j)]
        return dfs(0,0)

