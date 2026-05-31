class LinkNode:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None
        

class LRUCache:

    def __init__(self, capacity: int):
        self.kv = {} #key:LinkNode 
        self.left, self.right = LinkNode(0,0),LinkNode(0,0) # 양쪽 끝 pointer 
        self.left.next = self.right
        self.right.prev = self.left
        self.cp = capacity 

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev 
        
        

    def remove(self, node):
        prev, nxt = node.prev, node.next 
        prev.next = nxt
        nxt.prev = prev 
        

    def get(self, key: int) -> int:
        if key in self.kv:
            self.remove(self.kv[key])
            self.insert(self.kv[key])
            return self.kv[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.kv:
            self.remove(self.kv[key])
        self.kv[key] = LinkNode(key, value)
        self.insert(self.kv[key])

        
        if len(self.kv) > self.cp:
            lru = self.left.next 
            self.remove(lru)
            del self.kv[lru.key]
            


        
        
