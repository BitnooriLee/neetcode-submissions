class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0 
        visit = set()
        move = [(0,1),(1,0),(-1,0),(0,-1)]
        def bfs(i,j):
            q = deque()
            q.append([i,j])
            while q:
                x,y = q.popleft()
                for dx,dy in move:
                    if x+dx >=0 and x+dx<len(grid) and y+dy >=0 and y+dy<len(grid[0]) and grid[x+dx][y+dy] == "1":
                        q.append([x+dx,y+dy])
                        grid[x+dx][y+dy] = '0'
                
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    bfs(i,j) 
                    cnt += 1               
        return cnt 