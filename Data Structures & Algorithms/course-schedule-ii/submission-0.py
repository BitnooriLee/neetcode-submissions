class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = [0]*numCourses
        dic = defaultdict(list)
        output = []
        def dfs(course):
            if visited[course] == 1:
                return False
            if visited[course] == 2:
                return True
            visited[course] =1 

            for pre in dic[course]:
                if not dfs(pre):
                    return False
            visited[course] =2 
            output.append(course)
            return True 

        for p,c in prerequisites:
            dic[c].append(p)
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return output[::-1]  



        