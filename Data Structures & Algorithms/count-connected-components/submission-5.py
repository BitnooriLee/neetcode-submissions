class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dic = defaultdict(list)

        for s,d in edges:
            dic[s].append(d)
            dic[d].append(s)

        visited = []

        def dfs(cur,par):
            visited.append(cur)
            for nei in dic[cur]:
                if nei == par:
                    continue
                if nei in visited:
                    continue
                dfs(nei,cur)
            return True

        cnt = 0
        for i in range(0,n):
            if i not in visited:
                if dfs(i,-1):
                    cnt += 1
                    
        return cnt + n - len(visited)
            




        