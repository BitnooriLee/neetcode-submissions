class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0 

        res = 0 
        m,n = len(grid), len(grid[0])
        move = [(0,1), (1,0), (-1,0), (0,-1)]

        def dfs(i,j):
            if  i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
                return 0
            grid[i][j] = 2
            area = 1 
           
            for di,dj in move:
                area += dfs(i+di, j+dj)

            return area

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res,dfs(i,j))
        return res 



        