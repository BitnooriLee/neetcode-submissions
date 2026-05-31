class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []

        adj = defaultdict(list)
        for crs, pre in prerequisites:
            adj[pre].append(crs)
        status = [0] * numCourses

        def dfs(i):
            if status[i] == 1:
                return False
            if status[i] == 2:
                return True

            status[i] = 1
            for nxt in adj[i]:
                if not dfs(nxt):
                    return False 
            status[i] = 2
            res.append(i)
            return True


        for n in range(numCourses):
            if status[n] == 0:
                if not dfs(n):
                    return []
        return res[::-1]
                
            
        
        