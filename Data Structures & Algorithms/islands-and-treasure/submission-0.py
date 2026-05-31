class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        move = [(0,1),(1,0),(-1,0),(0,-1)]
        m = len(grid)
        n = len(grid[0])
        visit = set()
        q = deque()


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: #from gate 
                    q.append([i,j])
                    visit.add((i,j))

        dist = 0 
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                for dr, dc in move:
                    x, y  = r+dr, c+dc 
                    if (0<=x<m and 0<=y<n and (x,y) not in visit and grid[x][y] != -1):
                        visit.add((x,y))
                        q.append([x,y])

            dist += 1


        