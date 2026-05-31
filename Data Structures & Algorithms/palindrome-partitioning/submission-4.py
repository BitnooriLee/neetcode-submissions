class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.output = []
        path = []
        l = len(s)
        dp = [[False]*l for _ in range(l)] # [start][end]

        for i in range(l):
            dp[i][i] = True

        for length in range(2,l+1):
            for i in range(l-length+1):
                j = i + length -1 
                if s[i] == s[j] and (length <= 3 or dp[i+1][j-1] == True):
                    dp[i][j] = True


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
                if dp[start][i]:
                    path.append(s[start:i+1])
                    bt(i+1)
                    path.pop()


        bt(0)
        return self.output