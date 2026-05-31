class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        def getSum(n):
            s = 0 
            while(n>0):
                s += (n%10)*(n%10)
                n = n//10
            s+(n%10)*(n%10)
            return s

        while True:
            s = getSum(n)
            if s in seen:
                return False
            if s == 1:
                return True 
            else:
                seen.add(s)
                n = s 
            



                