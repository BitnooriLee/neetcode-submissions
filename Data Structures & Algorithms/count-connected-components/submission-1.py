class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges:
            return n 
        adj = [[] for _ in range(n)]
        visit = set()
        output = 0 
        def dfs(i):
            if i in visit:
                return 
            visit.add(i)
            for nei in adj[i]:
                if nei not in visit:
                    dfs(nei)


        
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        for i in range(n):
            if i not in visit:
                output+=1
                dfs(i)
        return output
        