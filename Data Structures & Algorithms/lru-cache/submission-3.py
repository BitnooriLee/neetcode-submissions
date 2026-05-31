class LinkList:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.dic = {} # key: LinkList, 
        self.capacity = capacity
        self.left, self.right = LinkList(0,0), LinkList(0,0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def add(self, node) -> None:
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev 

    def remove(self, node) -> None:
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key in self.dic:
            self.remove(self.dic[key])
            self.add(self.dic[key])
            return self.dic[key].val
        else: 
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.remove(self.dic[key])
        self.dic[key] = LinkList(key,value)
        self.add(self.dic[key])

        if len(self.dic) > self.capacity:
            lru = self.left.next 
            self.remove(lru)
            del self.dic[lru.key]
        
