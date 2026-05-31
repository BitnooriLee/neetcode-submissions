class DSU:
    def __init__(self,n):
        self.parent = list(range(n))
        self.level = [1]*n 
    def find(self,node):
        cur = node
        while self.parent[cur] != cur:
            self.parent[cur] = self.parent[self.parent[cur]]
            cur = self.parent[cur]
        return cur 

    def union(self,u,v):
        pv,pu = self.find(v), self.find(u)
        if pv == pu:
            return False
        if self.level[pv] > self.level[pu]:
            pv, pu = pu, pv
        self.parent[pv] = pu
        self.level[pu] += self.level[pv]
        return True

         
        
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        res = n 
        for u,v in edges:
            if dsu.union(u,v): #합쳐진다? 따로 있었다 
                res -= 1
        return res        
            
        






        