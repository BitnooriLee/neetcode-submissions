class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return 

        q = deque()
        m,n = len(grid), len(grid[0])
        move = [(0,1), (1,0), (-1,0), (0,-1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i,j))
        while q:
            i,j = q.popleft()
            for di, dj in move:
                ni,nj = i+di, j+dj
                if ni < 0 or ni >=m or nj < 0 or nj >= n:
                    continue 
                if grid[ni][nj] == -1:
                    continue
                nd = grid[i][j] + 1 
                if grid[ni][nj] > nd: # 갱신가능하면 
                    grid[ni][nj] = nd
                    q.append((ni,nj))

        return

                

  