class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        move = [(0,1), (0,-1), (1,0), (-1,0)]
        res = 0 

        def bfs(i,j):
            q= deque()
            grid[i][j] = "0"
            q.append((i,j))
            while q:
                x,y = q.popleft()
                for dx,dy in move:
                    if 0<=x+dx<m and 0<=y+dy<n and grid[x+dx][y+dy] == "1":
                        q.append([x+dx,y+dy])
                        grid[x+dx][y+dy] = "0"


        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    bfs(i,j)
                    res += 1

        return res