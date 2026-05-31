class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        res = 0 

        m,n = len(matrix), len(matrix[0])
        visit = set()
        move = [(1,0),(0,1),(0,-1),(-1,0)]
        dp = {} 

        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            best = 1
            
            for di,dj in move:
                ni,nj = i+di, j+dj
                if 0<= ni < m and 0<=nj<n and matrix[i][j] < matrix[ni][nj] and (ni,nj) not in visit:
                    best = max(best, dfs(ni,nj)+1)
                    dp[(i,j)] = best
            return best

                

        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i,j))

        return res 


        
        