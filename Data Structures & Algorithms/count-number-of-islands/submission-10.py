class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        move = [(0,1), (0,-1), (1,0), (-1,0)]
        res = 0 

        def bfs(x,y):
            grid[x][y] = -1
            for dx,dy in move:
                if 0<=x+dx<m and 0<=y+dy<n and grid[x+dx][y+dy] == "1":
                    bfs(x+dx,y+dy)


        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    bfs(i,j)
                    res += 1
                    grid[i][j] = "-1"


        return res