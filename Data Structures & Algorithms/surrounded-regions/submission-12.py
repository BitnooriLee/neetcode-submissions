class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m,n = len(board), len(board[0])
        move = [(0,1), (1,0), (-1,0), (0,-1)]
        q = deque()
        for i in range(m):
            if board[i][0] == "O":
                q.append([i,0])
                board[i][0] = "Y"
            if board[i][n-1] == "O":
                q.append([i,n-1])
                board[i][n-1] = "Y"
        for j in range(n):
            if board[0][j] == "O":
                q.append([0,j])
                board[0][j] = "Y"
            if board[m-1][j] == "O":
                q.append([m-1,j])
                board[m-1][j] = "Y"

        while q:
            x,y = q.popleft()
            for dx,dy in move:
                nx,ny = x+dx, y+dy
                if not (0<=nx<m and 0<=ny<n) or board[nx][ny]!= "O":
                    continue
                q.append([nx,ny])
                board[nx][ny] = "Y"

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
        for i in range(m):
            for j in range(n):    
                if board[i][j] == "Y":
                    board[i][j] = "O"
                
    