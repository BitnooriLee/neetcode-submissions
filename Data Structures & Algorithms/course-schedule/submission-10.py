class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for crs, pre in prerequisites:
            adj[crs].append(pre)

        status = [0] * numCourses
        def dfs(cur):
            if status[cur] == 2:
                return True
            if status[cur] == 1:
                return False
            
            status[cur] = 1
            for nxt in adj[cur]:
                if not dfs(nxt):
                    return False
            status[cur] = 2
            return True

        

        for c in range(numCourses):
            if status[c] == 0:
                if not dfs(c):
                    return False
        return True 



        