class Solution:
    def countBits(self, n: int) -> List[int]:
        def count(n):
            cnt = 0
            while(n):
                cnt+=1 
                n&=n-1
            return cnt 
        res = [0]*(n+1)
        for i in range(0,n+1):
            res[i] = count(i)

        return res