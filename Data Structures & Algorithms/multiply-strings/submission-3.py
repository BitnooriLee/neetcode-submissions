class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if len(num1)<len(num2):
            num1,num2 = num2, num1 
        m,n = len(num1), len(num2)

        res = 0 
        ws = 1 
        for i in range(m-1,-1,-1):
            w = 1 
            for j in range(n-1,-1,-1):
                res += int(num1[i])*ws*int(num2[j])*w
                w *= 10 
            ws*=10 
        return str(res)

        