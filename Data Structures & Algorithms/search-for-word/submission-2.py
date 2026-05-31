class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited = set()
        
        #cur: pointer in word
        def dfs(cur, i, j):
            if cur == len(word):
                return True

            if i < 0 or i >= m or j <0 or j>=n or board[i][j] != word[cur]:
                return False   
            #visited updates
            #before, after for loop, mark board[i][j] (prev val)
            tmp = board[i][j]
            board[i][j] = ""
            for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                if dfs(cur+1, i+dx, j+dy):
                    return True
            board[i][j] = tmp
            return False

        for i in range(m):
            for j in range(n):
                if dfs(0,i,j):
                    return True
        return False

        