class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return 

        m,n = len(board), len(board[0])
        
        move = [(0,1), (1,0), (-1,0), (0,-1)]
        def bfs(i,j):
            q = deque()
            q.append((i,j))
            board[i][j] = 'S'
            while q:
                x,y = q.popleft()
                for di,dj in move:
                    ni,nj = x+di, y+dj
                    if 0<= ni < m and 0<= nj<n and board[ni][nj] == 'O':
                        board[ni][nj] = 'S'
                        q.append((ni,nj))

        for i in range(0, m):
            if board[i][0] == 'O':
                bfs(i,0)
            if board[i][n-1] == 'O':
                bfs(i,n-1)
        for j in range(0, n):
            if board[0][j] == 'O':
                bfs(0,j)
            if board[m-1][j] == 'O':
                bfs(m-1,j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'

            
        