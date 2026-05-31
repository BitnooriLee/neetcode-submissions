class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = defaultdict(list)
        for cs, pre in prerequisites:
            dic[cs].append(pre)

        status = [0]*numCourses # 0 not visit, 1 visiting, 2 visited 

        def dfs(cur):
            if status[cur] == 2:
                return True
            if status[cur] == 1:
                return False

            status[cur] = 1 
            for pre in dic[cur]:
                if not dfs(pre):
                    return False

            status[cur] = 2
            return True

        for i in range(numCourses):
                if not dfs(i):
                    return False
        return True






        