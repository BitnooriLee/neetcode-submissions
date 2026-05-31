class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        m,n = len(grid), len(grid[0])
        move = [(0,1), (1,0), (-1,0), (0,-1)]
        q = deque()
        def bfs(i,j):
            while q:
                x,y = q.popleft()
                for dx,dy in move:
                    nx,ny = x+dx, y+dy
                    if 0<=nx<m and 0<=ny<n and grid[nx][ny] == INF:
                        grid[nx][ny] = grid[x][y]+1
                        q.append((nx,ny))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i,j))
        
        bfs(0,0)

        