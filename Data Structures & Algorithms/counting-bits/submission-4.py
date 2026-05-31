class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n+1):
            cnt = 0 
            while(i):
                i = i&(i-1)
                cnt+=1 
            output.append(cnt)

        return output