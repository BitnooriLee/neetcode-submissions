class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        direction = [(0,1), (1,0), (-1,0), (0,-1)]
        m,n = len(board), len(board[0])
        visited = [[False]*n for _ in range(m)]

        def backtrack(i,j,w):
            if board[i][j] != word[w]:
                return False
            if w == len(word)-1:
                return True

            visited[i][j] = True
            for dir in direction:
                ni,nj = i+dir[0], j+dir[1]
                if  0 > ni or ni >= m or 0 > nj or nj >= n:
                    continue
                if visited[ni][nj]:
                    continue
                if backtrack(ni,nj, w+1):
                    return True
            visited[i][j] = False
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if backtrack(i,j,0):
                        return True
        
        return False
        