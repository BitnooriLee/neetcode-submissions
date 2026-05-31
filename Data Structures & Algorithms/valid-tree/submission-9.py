class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(set)
        for s,d in edges:
            adj[s].add(d)
            adj[d].add(s)
        visited = set()

        def dfs(par, i):
            visited.add(i) 
            for nxt in adj[i]:
                if nxt == par:
                    continue 
                if nxt in visited:
                    return False
                if not dfs(i, nxt):
                    return False
            return True
        
        if not dfs(-1,0):
            return False
        return len(visited) == n 
        
        