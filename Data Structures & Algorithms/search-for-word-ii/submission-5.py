class Prefix:
    def __init__(self):
        self.children = {}
        self.word = None
   

        

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        m,n = len(board), len(board[0])
        #insert 
        root = Prefix()
        for w in words:
            node = root 
            for ch in w:
                if ch not in node.children:
                    node.children[ch] = Prefix()
                node = node.children[ch]    
            node.word = w 

        res = []
        move = [(0,1), (1,0), (-1,0), (0,-1)]
        
        def dfs(i,j, node):
            ch = board[i][j]
            if ch not in node.children:
                return
            nxt = node.children[ch]
            if nxt.word is not None:
                res.append(nxt.word)
                nxt.word = None
            board[i][j] = "#"
            for di,dj in move:
                ni,nj = i+di, j+dj
                if 0<=ni<m and 0<=nj<n and board[ni][nj] != "#":
                    dfs(ni,nj,nxt)
            board[i][j] = ch
            
        
        

        
        
        for i in range(m):
            for j in range(n):
                dfs(i,j, root)

        return res 
                    
        