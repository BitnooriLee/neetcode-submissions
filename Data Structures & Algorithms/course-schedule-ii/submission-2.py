class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        res = []

        for course,pre in prerequisites:
            dic[pre].append(course)

        state = [0] * numCourses

        def dfs(cur):
            if state[cur] == 2:
                return True
            if state[cur] == 1:
                return False

            state[cur] = 1
            for nxt in dic[cur]:
                if not dfs(nxt):
                    state[cur] = 0
                    return False
            state[cur] = 2
            
            res.append(cur)
            return True


        for i in range(numCourses):
            if state[i] == 0:
                if not dfs(i):
                    return []
        
        return res[::-1] 
        