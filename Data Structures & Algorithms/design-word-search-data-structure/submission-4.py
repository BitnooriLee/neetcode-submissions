class WordDictionary:

    def __init__(self):
        self.children = {}
        self.end_of_word = False
        

    def addWord(self, word: str) -> None:
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = WordDictionary()
            node = node.children[c]
        node.end_of_word = True

    def search(self, word: str) -> bool:
        node = self 
        def dfs(node,i):
            if i == len(word):
                return node.end_of_word
            ch = word[i]
            if ch != ".":
                if ch not in node.children:
                    return False
                return dfs(node.children[ch], i+1)
            for nxt in node.children.values():
                if dfs(nxt, i+1):
                    return True
            return False
        return dfs(self,0)
        
            
                
        
