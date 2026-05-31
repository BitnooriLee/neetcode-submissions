class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        l,r = len(num1), len(num2)
        res = 0 
        w = 1
        ws = 1 
        for i in range(l-1,-1,-1): 
            cur = 0 
            w = 1 
            for j in range(r-1,-1,-1):
                cur = int(num1[i])*int(num2[j])*w*ws
                res += cur 
                w = w*10 
            ws = ws*10
        return str(res)

        