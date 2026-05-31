class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        toVisit = set() #fresh orange 
        move = [(0,1), (1,0), (-1,0), (0,-1)]
        q = deque()
        count = 0 

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    toVisit.add((i,j))
                elif grid[i][j] == 2: 
                    q.append([i,j])
        
        while q and toVisit:
            for _ in range(len(q)):
                ci,cj = q.popleft()
                for di,dj in move:
                    x,y = ci+di, cj+dj
                    if 0<=x<m and 0<=y<n and (x,y) in toVisit:
                        toVisit.remove((x,y))
                        q.append([x,y])
            count += 1

        return -1 if toVisit else count


        