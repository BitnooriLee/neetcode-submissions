class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0 
        m,n = len(grid), len(grid[0])
        move = [(0,1), (1,0), (-1,0), (0,-1)]

        def bfs(i,j):
            area = 1 
            q = deque([(i,j)])
            while q:
                x,y = q.popleft()
                grid[x][y] = 2 
                for dx,dy in move:
                    nx,ny = x+dx, y+dy
                    if 0<=nx<m and 0<=ny<n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2 
                        q.append((nx,ny)) 
                        area += 1                      
            
            return area


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, bfs(i,j))
                   
        return res
        