class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False 

        dic = defaultdict(list)
        visit = set()
        
        for s,d in edges:
            dic[s].append(d)
            dic[d].append(s)

      

        def dfs(cur, par):
            visit.add(cur)
            for nxt in dic[cur]:
                if nxt == par:
                    continue
                if nxt in visit:
                    return False
                if not dfs(nxt, cur):
                    return False

            return True


        if not dfs(0,-1):
            return False

        return n == len(visit)
