class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m,n = len(board), len(board[0])
        move = [(0,1),(1,0),(0,-1),(-1,0)]

        #boarder -> T 
        def bfs(i,j):
            q = deque([(i,j)])
            board[i][j] = "T"
            while q:
                ci,cj = q.popleft()
                for di,dj in move:
                    x,y = ci+di, cj+dj
                    if 0<=x<m and 0<=y<n and board[x][y] == "O":
                        q.append((x,y))
                        board[x][y] = "T"

        
        #bfs for boardered O 

        for i in range(m):
            if  board[i][0] == "O":
                bfs(i,0)
            if board[i][n-1] == "O":
                bfs(i,n-1)
        for j in range(n):
            if  board[0][j] == "O":
                bfs(0,j)
            if board[m-1][j] == "O":
                bfs(m-1,j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "T":
                    board[i][j] = "O"


