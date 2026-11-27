class LL:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
class LRUCache:
   
    def __init__(self, capacity: int):
        self.dic = {} # key, node
        self.cap = capacity
        self.left, self.right = LL(None,None), LL(None,None)
        self.left.next, self.right.prev = self.right, self.left

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert(self, node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right 
        self.right.prev = node 

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        node = self.dic[key]
        self._remove(node)
        self._insert(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self._remove(self.dic[key])
        node = LL(key, value)
        self.dic[key] = node
        self._insert(node)

        if len(self.dic) > self.cap:
            lru = self.left.next
            self._remove(lru)
            del self.dic[lru.key]



  