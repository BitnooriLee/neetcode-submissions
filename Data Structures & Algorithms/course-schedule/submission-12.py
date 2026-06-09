class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = defaultdict(list)
        for cur, pre in prerequisites:
            dic[pre].append(cur) 
           

        state = [0] * numCourses
        #0 not visited, 1 visiting, 2 visited
        def dfs(cur):
            if state[cur] == 1:
                return False
            if state[cur] == 2:
                return True
            if state[cur] == 0:
                state[cur] = 1
                for pre in dic[cur]:
                    if not dfs(pre):
                        return False
                state[cur] = 2
            return True


        for crs in range(numCourses):
            if state[crs] == 0:
                if not dfs(crs):
                    return False
        return True 



            

        