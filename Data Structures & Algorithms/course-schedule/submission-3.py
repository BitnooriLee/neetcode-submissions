class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        dic = defaultdict(list)
        for course, pre in prerequisites:
            dic[pre].append(course)
        
        state = [0] * numCourses

        def dfs(cur):
            if state[cur] == 2:
                return True
            if state[cur] == 1:
                return False #cycle

            state[cur] = 1 
            for nxt in dic[cur]:
                if not dfs(nxt):
                    return False
            state[cur] = 2 
            return True

            
        for i in range(numCourses):
            if state[i] == 0:
                if not dfs(i):
                    return False

        return True
            

    





