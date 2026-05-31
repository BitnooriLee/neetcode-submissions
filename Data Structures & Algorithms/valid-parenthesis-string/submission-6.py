class Solution:
    def checkValidString(self, s: str) -> bool:
        l = len(s)
        low,high = 0,0
   
        for i in range(l):
            if s[i] == "(":
                high += 1
                low += 1 
            elif s[i] == ")":
                high -= 1
                low -= 1  
            elif s[i] == "*":
                high+= 1
                low -= 1  
            else: return False

            if high < 0:
                return False
            if low < 0 :
                low = 0
        return low == 0
 