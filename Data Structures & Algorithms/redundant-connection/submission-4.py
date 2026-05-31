class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n 

    def find(self, node):
        cur = node
        while cur != self.parent[cur]:
            self.parent[cur] = self.parent[self.parent[cur]]
            cur =  self.parent[cur]
        return cur
    def union(self, u,v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False

        if self.rank[pu] < self.rank[pv]:
            pu, pv = pv, pu
        self.rank[pu] += self.rank[pv]
        self.parent[pv] = pu 
        return True
        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges)+1)
        for u,v in edges:
            if not dsu.union(u,v):
                return [u,v]
        return [-1,-1]
            
            
        