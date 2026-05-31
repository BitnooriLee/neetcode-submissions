class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        q = deque()
        dis = 0 
        move = [(0,1),(1,0),(-1,0),(0,-1)]
        fresh = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1

        while q and fresh > 0:
            l = len(q)
            for _ in range(l):
                x,y = q.popleft()
                for dx,dy in move:
                    nx,ny = x+dx,y+dy
                    if not(0<=nx<m and 0<=ny<n):
                        continue
                    if grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1 
                        q.append((nx,ny))
            dis += 1

        return dis if fresh == 0 else -1 








        