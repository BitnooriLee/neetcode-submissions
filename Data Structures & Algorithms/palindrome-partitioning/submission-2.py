class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def isPal(l,r):
            while(l<r):
                if s[l]!=s[r]:
                    return False
                l+= 1
                r-= 1
            return True 


        def backtrack(start):
            
            if start == len(s):
                res.append(path[:])
            for end in range(start, len(s)):
                if isPal(start,end):
                    path.append(s[start:end+1])
                    backtrack(end+1)
                    path.pop()

        backtrack(0)
        return res
        