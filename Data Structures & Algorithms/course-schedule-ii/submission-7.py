class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        status = [0]*numCourses
        res = []
        for course, pre in prerequisites:
            dic[pre].append(course)

        def dfs(i):
            if status[i] == 2:
                return True
            if status[i] == 1:
                return False
            status[i] = 1
            for nxt in dic[i]:
                if not dfs(nxt):
                    status[i] = 0
                    return False
            status[i] = 2
            res.append(i)
            return True


        for i in range(numCourses):
            if status[i] == 0:
                if not dfs(i):
                    return []
        return res[::-1]

        