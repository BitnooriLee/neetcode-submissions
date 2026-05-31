class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        move = [(0,1),(1,0),(-1,0),(0,-1)]
        output = 0 

        def bfs(i,j):
            nonlocal output
            q = deque([(i,j)]) #튜플이 하나씩들어간 리스트 만듬
            while q:
                x,y = q.popleft()
                grid[x][y] = "2"
                for dx,dy in move:
                    nx,ny = x+dx, y+dy
                    if 0<=nx<m and 0<=ny<n:
                        if grid[nx][ny] == "1":
                            q.append((nx,ny)) #리스트에 튜플을 append해줌.. []x 
                    

        for i in range(m):
            for j in range(n): 
                if grid[i][j] == "1":
                    bfs(i,j)
                    output += 1
        return output

        