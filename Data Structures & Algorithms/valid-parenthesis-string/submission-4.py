class Solution:
    def checkValidString(self, s: str) -> bool:
        if len(s)==1:
            if s == "*":
                return True
            else: 
                return False 

        stk = 0
        star = 0
        
        for ch in s:
            if ch == "(":
                stk += 1
            elif ch == "*":
                star += 1 
            else:
                stk -= 1 
            if stk < 0:
                if star > 0:
                    star -= 1 
                    stk += 1 
                else:
                    return False
        if stk > star:
            return False

        star, rstk = 0,0
        for i in range(len(s)-1,-1,-1):
            ch = s[i]
            if ch == ")":
                rstk += 1
            elif ch == "*":
                star += 1 
            else:
                rstk -= 1 
            if rstk < 0:
                if star > 0:
                    star -= 1 
                    rstk += 1 
                else:
                    return False
        if rstk > star:
            return False
        
        return True
            

        