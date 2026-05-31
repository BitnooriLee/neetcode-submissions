class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        move = [(0,1),(1,0),(-1,0),(0,-1)]
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh +=1 
        q = deque()
        t = 0 

        def bfs(i,j):
            nonlocal fresh,t
            while q and fresh > 0:
                l = len(q)
                for _ in range(l):
                    x,y = q.popleft()
                    for dx,dy in move:
                        nx,ny = x+dx, y+dy 
                        if 0<=nx<m and 0<=ny<n and grid[nx][ny] == 1:
                            fresh -=1 
                            grid[nx][ny] = 2 
                            q.append((nx,ny))
                t+=1 
                    
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
        bfs(0,0)

        return t if fresh == 0 else -1