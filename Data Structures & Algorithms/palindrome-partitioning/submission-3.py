class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.output = []
        path = []
        l = len(s)

        def isPal(arr):
            l,r = 0, len(arr)-1
            while(l<r):
                if arr[l]!= arr[r]:
                    return False
                l+=1
                r-=1
            return True

        def bt(start):
            if start == l:
                self.output.append(path[:])
                return 
            for i in range(start,l):
                if isPal(s[start:i+1]):
                    path.append(s[start:i+1])
                    bt(i+1)
                    path.pop()


        bt(0)
        return self.output