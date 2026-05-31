class Solution:
    def isHappy(self, n: int) -> bool:

        check = set()
        def isSum(n):
            squreSum = 0
            while n//10:
               squreSum += (n%10)*(n%10)
               n = n//10 
            squreSum += n*n 

            return squreSum
        tmp = isSum(n)
        while True: 
            if tmp == 1:
                return True
            elif tmp in check:
                return False
            else:
                check.add(tmp)
                tmp = isSum(tmp)

        