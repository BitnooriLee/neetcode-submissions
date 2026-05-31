class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0 

        res = 0 
        m,n = len(grid), len(grid[0])
        move = [(0,1),(1,0),(-1,0),(0,-1)]

        def dfs(i,j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != "1":
                return 
            grid[i][j] = "2"
            for di,dj in move:
                dfs(i+di, j+dj)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1 
                    dfs(i,j)
        return res 
        