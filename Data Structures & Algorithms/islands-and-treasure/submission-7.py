class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m,n = len(grid), len(grid[0])
        INF = 2147483647
        move = [(0,1),(1,0),(-1,0),(0,-1)]
        q= deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: #inf 아니면 방문했던 곳 
                    q.append((i,j))

        while q:
            x,y = q.popleft()
            for dx,dy in move:
                nx,ny = x+dx,y+dy
                if not( 0<=nx<m and 0<=ny<n):
                    continue
                if grid[nx][ny] != INF: # 벽-1, 0, 이미 채워진칸은 스킵
                    continue
                grid[nx][ny] = grid[x][y]+1
                q.append((nx,ny))
        return

    
                    