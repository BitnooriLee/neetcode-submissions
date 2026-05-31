class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #check cycle?
        #all connected?

        adj = defaultdict(set)
        for s,e in edges:
            adj[s].add(e)
            adj[e].add(s)
        visited = set()

        

        def dfs(par, cur):
            visited.add(cur)
            for nxt in adj[cur]:
                if nxt == par:
                    continue
                if nxt in visited:
                    return False
                if not dfs(cur, nxt):
                    return False
            return True

      

        if not dfs(-1,0):
            return False
        return len(visited) == n


