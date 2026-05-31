class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}
        m,n = len(word1), len(word2)

        def dfs(i,j):
           
            if i == m:
                return n-j
            if j == n:
                return m-i
            if (i,j) in dp:
                return dp[(i,j)]
            if word1[i] != word2[j]:
                insert = 1+ dfs(i+1,j)
                delete = 1+ dfs(i,j+1)
                replace = 1+ dfs(i+1,j+1)

                dp[(i,j)] = min(insert, delete, replace)
            else:
                dp[(i,j)] = dfs(i+1,j+1)

            return dp[(i,j)]

        return dfs(0,0)