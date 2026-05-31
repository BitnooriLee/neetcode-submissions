class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        move = [(0,1), (1,0), (-1,0), (0,-1)]
 
        m,n = len(matrix), len(matrix[0])
        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            best =1 
            for di,dj in move:
                if 0<=i+di<m and 0<=j+dj<n and matrix[i+di][j+dj] > matrix[i][j]:
                    best = max(best, dfs(i+di,j+dj)+1)
                    dp[(i,j)] = best 

            return best 
    
        res = 0 
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i,j))
        
        return res