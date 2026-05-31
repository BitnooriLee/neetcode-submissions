class DSU:
    def __init__(self, l):
        self.parent = list(range(l))
        self.rank = [1]*l
    def find(self, node):
        cur = node
        while cur != self.parent[cur]:
            self.parent[cur] =self.parent[self.parent[cur]] 
            cur = self.parent[cur]
        return cur

    def union(self, u,v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.rank[pv] > self.rank[pu]:
            pv,pu = pu,pv 
        self.parent[pv] = pu
        self.rank[pu] += self.rank[pv]
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges)+1)
        for u,v in edges:
            if not dsu.union(u,v):
                return [u,v]
        return [-1,-1]

        