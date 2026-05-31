class PrefixTree:

    def __init__(self):
        self.chilren = {}
        self.end_of_word = False
        

    def insert(self, word: str) -> None:
        node = self 
        for ch in word:
            if ch not in node.chilren:
                node.chilren[ch] = PrefixTree()
            node = node.chilren[ch]
        node.end_of_word = True

    def search(self, word: str) -> bool:
        node = self 
        for ch in word:
            if ch not in node.chilren:
                return False
            node = node.chilren[ch]
        return node.end_of_word 
        

    def startsWith(self, prefix: str) -> bool:
        node = self 
        for ch in prefix:
            if ch not in node.chilren:
                return False
            node = node.chilren[ch]
        return True
        
        