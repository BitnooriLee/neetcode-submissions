class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        INF = 2147483647
        

        #return distance 
        def bfs(i,j):
            q= deque([(i,j)])
            visited = [[False]*n for _ in range(m)]
            visited[i][j] = True
            distance = 0 
            while q:
                for _ in range(len(q)):
                    x,y = q.popleft()
                    if grid[x][y] == 0:
                        return distance
                    for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                        if x+dx >= 0 and x+dx < m and y+dy >=0 and y+dy < n and not visited[x+dx][y+dy] and grid[x+dx][y+dy] != -1:
                            visited[x+dx][y+dy] = True
                            q.append((x+dx, y+dy)) 
                distance += 1 
            return INF




        for i in range(m):
            for j in range(n): 
                if grid[i][j] == INF:
                    grid[i][j] = bfs(i,j)


        