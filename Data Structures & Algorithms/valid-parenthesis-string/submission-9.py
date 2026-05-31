class Solution:
    def checkValidString(self, s: str) -> bool:
        lowerbound, upperbound = 0,0

        for ch in s:
            if ch == "(":
                upperbound += 1
                lowerbound += 1

            elif  ch == ")":
                upperbound -= 1
                lowerbound -= 1
            elif ch == "*":
                upperbound += 1
                lowerbound -= 1
            else:
                return False
        
            if upperbound < 0:
                return False      
            if lowerbound < 0 :
                lowerbound = 0 

        return lowerbound == 0