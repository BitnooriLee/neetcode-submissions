class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0 
        while(n): #1일때도 
            cnt+= 1
            n &=(n-1) #가장 오른쪽 1사라짐 
        return cnt