class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        if not board or not board[0]:
            return

        m,n = len(board),len(board[0])
        visited = [[False] * n for _ in range(m)]
        move = [(0,1),(1,0),(-1,0),(0,-1)]
        
        
        def bfs(x,y):
            q = deque()
            q.append((x,y))
            visited[x][y] = True

            region = []
            touch_border = False
            while q:
                i,j = q.popleft()
                region.append((i,j))
                
                if i == 0 or i == m -1 or j == 0 or j == n -1:
                    touch_border = True 
                for di, dj in move:
                    ni,nj = i+di, j+dj
                    if ni >=0 and ni < m and nj >=0 and nj < n:
                        if not visited[ni][nj] and board[ni][nj] == 'O':
                            visited[ni][nj] = True
                            q.append((ni,nj))
            
            if not touch_border:
                for a,b in region:
                    board[a][b] = "X"


        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and not visited[i][j]:
                    bfs(i,j)

        return