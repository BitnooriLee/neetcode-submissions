class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [0]*numCourses #not visited
        dic = defaultdict(list)

        def dfs(coure):
            if visited[coure] == 1:
                return False
            if visited[coure] == 2:
                return True
            # not visited, iterate 
            visited[coure] = 1

            # iterate prerequisites 
            for pre in dic[coure]:
                if not dfs(pre):
                    return False
            visited[coure] = 2 
            return True

        #adjlist 
        for pre, crs in prerequisites:
            dic[crs].append(pre)

        #check every course
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True 
            

        