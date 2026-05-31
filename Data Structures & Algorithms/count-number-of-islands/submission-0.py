class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        move = [(0,1),(1,0),(-1,0),(0,-1)]
        m,n = len(grid), len(grid[0])
        count = 0 
        def bfs(i,j,grid):
            q = deque([(i,j)])
            while q:
                print(q)
                ci,cj  = q.popleft()
                for di,dj in move:
                    if 0<=ci+di<m and 0<=cj+dj<n and grid[ci+di][cj+dj] == "1":
                        q.append((ci+di, cj+dj))
                        grid[ci+di][cj+dj] = "0" 

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    bfs(i,j,grid)
                    count += 1

        return count


    
        