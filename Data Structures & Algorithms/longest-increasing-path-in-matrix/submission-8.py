class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix), len(matrix[0])
        move = [(0,1), (1,0), (-1,0), (0,-1)]

        dp = {}

        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            cur = 1
            for di,dj in move:
                ni,nj = i+di, j+dj
                if 0<=ni<m and 0<=nj<n and matrix[i][j] < matrix[ni][nj]:
                    cur = max(cur,dfs(ni,nj)+1)
                dp[(i,j)] = cur
            return cur 
        res = 0 
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i,j))
        return res