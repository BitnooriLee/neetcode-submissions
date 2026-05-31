class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n+1))
        rank = [0] * (n+1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]


        def union(x,y):
            p1, p2 = find(x), find(y)
            if p1 == p2:
                return False
            if rank[p1]>rank[p2]:
                parent[p2] = p1
            elif rank[p1]<rank[p2]:
                parent[p1] = p2 
            else:
                parent[p1] = p2 
                rank[p2]+= 1
            return True

        for s,d in edges:
            if not union(s,d):
                return [s,d]


        