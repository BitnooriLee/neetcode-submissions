class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False 

        dic = defaultdict(list) # order x 
        
        for s,d in edges:
            dic[s].append(d)
            dic[d].append(s)

        visited = set()
        def dfs(cur, par):   
            visited.add(cur)
            for des in dic[cur]:
                if des == par:
                    continue
                if des in visited:
                    return False
                if not dfs(des,cur):
                    return False
            return True


        if not dfs(0,-1):
            return False 

        return len(visited) == n
            