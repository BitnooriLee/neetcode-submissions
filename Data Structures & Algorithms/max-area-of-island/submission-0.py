class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        move = [(0,1),(1,0),(-1,0),(0,-1)]
        output = 0 # max num 
        
        def dfs(i,j,grid):
            grid[i][j] = 0 
            tmp = 1
            for di, dj in move:
                x,y = i+di, j+dj
                if 0<=x<m and 0<=y<n and grid[x][y] == 1:
                        tmp += dfs(x,y,grid)       
            return tmp

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    tmp = dfs(i,j,grid)
                    output = max(output, tmp)

        return output 

        