class DSU:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [1]*n 

    def find(self,node):
        cur = node
        while cur != self.parent[cur]:
            self.parent[cur] = self.parent[self.parent[cur]]
            cur = self.parent[cur]
        return cur 

    def union(self, u,v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False
        if self.rank[u] > self.rank[v]:
            pu, pv = pv, pu
        self.parent[pu] = pv
        self.rank[pv] += self.rank[pu]
        return True




class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges)+1)

        for s,d in edges:
            if not dsu.union(s,d):
                return [s,d]

        return [-1,-1]
