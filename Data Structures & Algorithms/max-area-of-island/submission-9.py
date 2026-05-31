class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        res = 0
        move = [(0,1),(1,0),(-1,0),(0,-1)]

        def bfs(i,j):
            q= deque([(i,j)])
            cur = 0
            grid[i][j] = 2
            while q:
                x,y = q.popleft()
                cur += 1
                for dx,dy in move:
                    nx,ny = x+dx, y+dy
                    if 0<=nx<m and 0<=ny<n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        q.append((nx,ny))
            return cur


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cur = bfs(i,j)
                    res = max(res, cur)

        return res



        