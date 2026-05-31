class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        output = 0 
        move = [(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(i,j):
            
            if i < 0 or i >= len(grid) or j <0 or j >= len(grid[0]) or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            area = 1 
            for di,dj in move:
                area += dfs(i+di,j+dj)
            return area


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    cur = dfs(i,j)
                    
                    output = max(output, cur)

        return output
        