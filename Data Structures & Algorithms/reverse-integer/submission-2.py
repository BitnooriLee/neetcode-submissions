class Solution:
    def reverse(self, x: int) -> int:
        left,right = -2**31, 2**31-1
        if left > x or x > right:
            return 0
        
        sign = 1 if x >=0 else -1 
        x = abs(x)

        res = 0 

        while(x):
            if res > right // 10 or (res == right // 10 and x%10 > 7):
                return 0
            res = res*10 + x%10
            x = x//10
       
        return sign*res  
        
        