class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board), len(board[0])
        d = [(0,1),(0,-1),(1,0),(-1,0)]
        visit = set()
        tmp = []
        def bt(i,x,y): 
            if i == len(word):
                return True
            for dx,dy in d:
                if 0<=x+dx<m and 0<=y+dy<n and board[x+dx][y+dy] == word[i] and (x+dx, y+dy) not in visit:
                    visit.add((x+dx,y+dy))
                    if bt(i+1, x+dx,y+dy):
                        return True
                    visit.remove((x+dx,y+dy))
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visit.add((i,j))
                    if bt(1,i,j):
                        return True
                    visit.remove((i,j))
                    
        return False