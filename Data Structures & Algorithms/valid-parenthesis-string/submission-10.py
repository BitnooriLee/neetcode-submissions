class Solution:
    def checkValidString(self, s: str) -> bool:
        op,cl = 0,0 
        for ch in s:
            if ch == "(":
                op += 1 
                cl += 1
            elif ch == ")":
                op -= 1
                cl -= 1
            elif ch == "*":
                op += 1
                cl -= 1 
            else:
                return False
            if op < 0:
                return False
            if cl < 0:
                cl = 0
                
        return cl == 0 