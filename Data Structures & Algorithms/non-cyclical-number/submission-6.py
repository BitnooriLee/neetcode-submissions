class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        cur = n 
        while True:
            res = 0 
            while(cur):
                res += (cur%10)*(cur%10) 
                cur //= 10 
            print(res)
            if res == 1:
                return True 
            if res in seen:
                return False
            seen.add(res)
            cur = res 


        