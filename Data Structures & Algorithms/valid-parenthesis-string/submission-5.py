class Solution:
    def checkValidString(self, s: str) -> bool:
        
        lo,hi = 0,0 

        for ch in s:
            if ch == "(":
                hi += 1 
                lo += 1
            elif ch == ")":
                hi -= 1
                lo -= 1

            else: # 범위를 넓혀줌 
                hi += 1 
                lo -= 1 

            if hi < 0: # ) 너무 많음
                return False
            
            if lo < 0:
                lo = 0 

        return lo == 0
        