class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visit = [0] * numCourses #0 not visited, 1 visited, 2 took 
        dic = defaultdict(list)
        output = []
        def dfs(course):
            if visit[course] == 1:
                return False
            if visit[course] == 2:
                return True
            visit[course] = 1 

            for pre in dic[course]:
                if not dfs(pre):
                    return False
            visit[course] =2 
            output.append(course)
            return True


        for course,pre in prerequisites:
            dic[course].append(pre)

        for i in range(numCourses):
            if not dfs(i):
                return []
        return output
            





        
        