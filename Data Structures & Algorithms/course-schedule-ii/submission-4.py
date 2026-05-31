class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        st = [0]*numCourses # 0 not visited, 1 visiting 2 done

        dic = defaultdict(list) #course: pre 
        output = []
        for course, pre in prerequisites:
            dic[pre].append(course)

    
        def dfs(i):
            if st[i] == 2:
                return True
            if st[i] == 1:
                return False
            st[i] = 1
            for nxt in dic[i]:
                if not dfs(nxt):
                    st[i] = 0
                    return False
            st[i] = 2 
            output.append(i)
            return True

        for i in range(numCourses):
            if st[i] == 0:
                if not dfs(i):
                    return []

        return output[::-1]