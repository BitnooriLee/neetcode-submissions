class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dic = defaultdict(list)

        for s,d in edges:
            dic[s].append(d)
            dic[d].append(s)

        visit = set()
        res = 0 


        def dfs(cur, par): 
            visit.add(cur) 
            for nxt in dic[cur]:
                if nxt == par:
                    continue
                if nxt in visit: #이미 다른 그룹에 들어갔을 수 있음?
                    continue
                dfs(nxt, cur)
            
            

        for i in range(n):
            if i not in visit:
                dfs(i,-1)
                res+= 1 

        return res



        


        