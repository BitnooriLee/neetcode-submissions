class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None 

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = TrieNode() # 빈걸로 시작 
        res = []
        move = [(0,1),(1,0),(-1,0),(0,-1)]
        m,n = len(board), len(board[0])
        for w in words:
            node = root 
            for ch in w:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = w #마지막에 word를 넣어줌 끝 체크 

        def dfs(i,j, node): 
            ch = board[i][j]
            if ch not in node.children:
                return 
            nxt = node.children[ch]
            if nxt.word is not None: 
                res.append(nxt.word)
                nxt.word = None # 중복방지 

            board[i][j] = '#' # 방문 처리 
            for di,dj in move:
                ni,nj = i+di, j+dj
                if ni >= 0 and ni < m and nj >=0 and nj < n and board[ni][nj] != '#':
                    dfs(ni,nj,nxt)
            board[i][j] = ch 

            if not nxt.children and nxt.word is None: #더이상 탐색할 필요 없음 
                node.children.pop(ch, None) 

        for i in range(m):
            for j in range(n):
                dfs(i,j, root)
        return res





        