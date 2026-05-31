class LL:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.nxt = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {} # key to node 
        self.left, self.right = LL(0,0), LL(0,0)
        self.left.nxt, self.right.prev = self.right, self.left 
    
    
    #node 연결 업뎃 
    def add(self,node):
        prev, next = self.right.prev, self.right 
        prev.nxt = next.prev = node
        node.nxt, node.prev = next, prev
        node.prev = prev


        
    def remove(self,node):
        prev, next = node.prev, node.nxt
        prev.nxt = next
        next.prev = prev 

    def get(self, key: int) -> int:
        if key in self.dic:
            # LRU update 
            self.remove(self.dic[key])
            self.add(self.dic[key])
            return self.dic[key].val 
        else:
            return -1 
        

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.remove(self.dic[key])
        self.dic[key] = LL(key, value)
        self.add(self.dic[key])

        if len(self.dic) > self.capacity:
            lru = self.left.nxt 
            self.remove(lru)
            del self.dic[lru.key] #LL도 key를 가지고 있음! 
            
        
        
