class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        toVisit = set() # fresh orange 
        dis = 0 
        q= deque()
                

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    toVisit.add((i,j))
                if grid[i][j] == 2:
                    q.append([i,j])

        while q and toVisit:
            for _ in range(len(q)):
                x,y = q.popleft()
                for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                    nx,ny = x+dx, y+dy
                    if 0<=nx<m and 0<=ny<n and (nx,ny) in toVisit:
                        toVisit.remove((nx,ny))
                        q.append((nx,ny))
            dis+=1 
                    

        return -1 if toVisit else dis 
             
        