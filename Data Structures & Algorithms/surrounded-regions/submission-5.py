class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m,n = len(board), len(board[0])
        move = [(0,1),(1,0),(-1,0),(0,-1)]

        #check border O and change to T 
        def bfs():
            q = deque()
            for i in range(m):
                for j in range(n):
                    if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and board[i][j] == "O":
                        q.append((i,j))

            while q:
                r,c = q.popleft()
                if board[r][c] == "O":
                    board[r][c] = "T"
                    for di,dj in move:
                        ni, nj = r+di, c+dj
                        if 0<= ni < m and 0 <= nj < n:
                            q.append((ni,nj))

        bfs()     
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"
                    
        