class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPal(i,j):
            while (i<j):
                if s[i] != s[j]:
                    return False
                i+=1 
                j-=1
            return True
        path = []
        res = []

        def bt(start):
            nonlocal path
            if start == len(s):
                res.append(path[:])
                return 
            for end in range(start, len(s)):
                if isPal(start,end):
                    path.append(s[start:end+1])
                    bt(end+1)
                    path.pop()
            

        bt(0)
        return res



        