class PrefixTree:

    def __init__(self):
        self.children = {}
        self.end_of_word = False
        

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = PrefixTree()
            node = node.children[ch]
        node.end_of_word = True
                
    def search(self, word: str) -> bool:
        node = self
        for ch in word:
            if ch not in node.children:
                return Falase
            node = node.children[ch]
        return node.end_of_word 
        
    def startsWith(self, prefix: str) -> bool:
        node = self
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True
        
        