class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #cycle?
        # visit all n? 
        if len(edges) < n-1:
            return False
        adj = [[] for _ in range(n)]
        visit = set()
        for s,e in edges:
            adj[s].append(e)
            adj[e].append(s)

        def dfs(node, par):
            if node in visit:
                return False
            visit.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                #node -> nei visited
                if not dfs(nei, node):
                    return False
            return True

        return dfs(0,-1) and len(visit) == n 