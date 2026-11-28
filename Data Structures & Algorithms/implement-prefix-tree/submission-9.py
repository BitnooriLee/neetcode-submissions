class PrefixTree:

    def __init__(self):
        self.endofstr = False
        self.children = {}
        
    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = PrefixTree()
            node = node.children[ch]
        node.endofstr = True

    def search(self, word: str) -> bool:
        node = self
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.endofstr 
        

    def startsWith(self, prefix: str) -> bool:
        node = self
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True
        
        
        