class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []
        path = []

        def isPal(l,r):
            while(l<r):
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True 

        def bt(i):
            if i == len(s):
                res.append(path[:])
                return 
            for j in range(i, len(s)):
                if isPal(i,j):
                    path.append(s[i:j+1])
                    bt(j+1)
                    path.pop()

        bt(0)

        return res
                



        