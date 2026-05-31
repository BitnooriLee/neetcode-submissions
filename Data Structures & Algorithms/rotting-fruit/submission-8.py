class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0 
        fresh = set()
        q = deque()
        res = 0 
        m,n = len(grid), len(grid[0])
        move = [(0,1), (1,0), (-1,0), (0,-1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh.add((i,j))
                elif grid[i][j] == 2:
                    q.append((i,j))

        cnt = 0
        while q and fresh:
            l = len(q)
            for _ in range(l):
                i,j = q.popleft()
                for di,dj in move:
                    ni,nj = i+di, j+dj
                    if ni<0 or ni>=m or nj<0 or nj>=n:
                        continue
                    if grid[ni][nj] == 0:
                        continue
                    if grid[ni][nj] == 1:
                        grid[ni][nj] = 2 
                        q.append((ni,nj))
                        fresh.remove((ni,nj))
                   
            cnt+= 1 
        return -1 if fresh else cnt

                

        
        