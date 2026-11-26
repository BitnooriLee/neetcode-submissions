class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        seen.add(n)
        def cal(num):
            sum = 0 
            while(num):
                r = num%10
                num = num//10
                sum += r*r 
            return sum 

        while True:
            n = cal(n)
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)
            
        return False
        
            

   
        