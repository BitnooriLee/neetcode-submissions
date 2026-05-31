class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n = len(heights), len(heights[0])
        pacific = set()
        atlantic = set() 
        res = []
        move = [(0,1),(1,0),(-1,0),(0,-1)]
        
        def dfs(r,c, visit, preHeight):
            if (r,c) in visit or r<0 or r>= m or c<0 or c>=n or heights[r][c] < preHeight:
                return 
            visit.add((r,c))
            for di, dj in move:
                dfs(r+di, c+dj, visit, heights[r][c])

        for j in range(n):
            dfs(0,j,pacific, heights[0][j])
            dfs(m-1,j,atlantic,heights[m-1][j])
        for i in range(m):
            dfs(i,0,pacific,heights[i][0])
            dfs(i,n-1,atlantic,heights[i][n-1])
       
        for i in range(m):
            for j in range(n):
                if (i,j) in pacific and (i,j) in atlantic:
                    res.append([i,j])

        return res


                

        