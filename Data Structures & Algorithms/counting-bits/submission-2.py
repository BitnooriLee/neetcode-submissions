class Solution:
    def countBits(self, n: int) -> List[int]:
        def cnt(n):
            c = 0 
            while(n):
                n&=(n-1)
                c+=1
            return c
        output = []
        for i in range(n+1):
            res = cnt(i)
            output.append(res)

        return output