class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not n:
            return 0
        #adjacent
        adj = {i:[] for i in range(n)}

        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        visit = set()
        def dfs(i):
            if i in visit:
                return 
            visit.add(i)
            for j in adj[i]:
                dfs(j)
        cnt = 0 
        for i in range(n):
            if i not in visit:
                cnt += 1 
                dfs(i)
        return cnt 

        
        