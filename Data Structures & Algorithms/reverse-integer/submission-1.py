class Solution:
    def reverse(self, x: int) -> int:
        left,right = -2**31, 2**31-1
        if left > x or x > right:
            return 0
        if x >=0:
            sign = 1
        else: 
            sign = -1

        if sign -1: 
            x = -x 

        res = 0 

        while(x):
            res = res*10 + x%10
            x = x//10
        print(res)
        if left > sign*res  or sign*res  > right:
            return 0
        else: return sign*res  
        
        