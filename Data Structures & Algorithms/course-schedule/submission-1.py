class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        status = [0]*numCourses #0 not visited, 1 visited 2 took the course
        dic = defaultdict(list) 
        
        def dfs(course):
            if status[course] == 1:
                return False
            if status[course] == 2:
                return True
            #not visited
            status[course] = 1

            for pre in dic[course]:
                #check if pre can be taken
                if not dfs(pre):
                    return False
            status[course] = 2 
            return True
 
        # adj dic 
        for course, pre in prerequisites:
            dic[course].append(pre)

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True 



        