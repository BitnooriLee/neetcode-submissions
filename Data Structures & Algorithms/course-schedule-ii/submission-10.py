class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for course, pre in prerequisites:
            adj[pre].append(course)

        status = [0] * numCourses
        res = []
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
            res.append(cur)
            return True
        for i in range(numCourses):
            if status[i] == 0:
                if not dfs(i):
                    return []
        return res[::-1]

