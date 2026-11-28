class WordDictionary:

    def __init__(self):
        self.eow = False
        self.children = {}

    def addWord(self, word: str) -> None:
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = WordDictionary()
            node = node.children[ch]
        node.eow = True

    def search(self, word: str) -> bool:

        def dfs(i,node):
            if i == len(word):
                return node.eow
            ch = word[i]
            if ch != ".":
                if ch not in node.children:
                    return False
                return dfs(i+1,node.children[ch])
            for nxt in node.children.values():
                if dfs(i+1, nxt):
                    return True
            return False
            
        return dfs(0, self)
        
