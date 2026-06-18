class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #all connected, no cycle 
        visited = set()
        dic = defaultdict(set)
        for s,d in edges:
            dic[s].add(d)
            dic[d].add(s)
        def dfs(par,i):
            visited.add(i)
            for nxt in dic[i]:
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

        