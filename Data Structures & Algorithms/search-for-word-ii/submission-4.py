class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        #insert 
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word # 마지막에 word 넣어줌 

        res = []
        move = [(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(i,j, node):
            #search 
            ch = board[i][j]
            if ch not in node.children:
                return
            nxt = node.children[ch]
            if nxt.word is not None:
                res.append(nxt.word)
                nxt.word = None # 중복방지 
            board[i][j] = "#" #사이클 방지 
            for di,dj in move:
                ni,nj = i+di, j+dj
                if 0<=ni<len(board) and 0<=nj<len(board[0]) and board[ni][nj] != "#":
                    dfs(ni,nj,nxt)
            board[i][j] = ch

            
        


        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i,j,root)
        return res 
