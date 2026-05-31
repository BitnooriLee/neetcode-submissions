class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for ch in tokens:
            if ch in "+-*/":
                num2 = stk.pop()
                num1 = stk.pop()
                if ch == "+":
                    stk.append(num1+num2)
                elif ch == "-":
                    stk.append(num1-num2)
                elif ch == "*":
                    stk.append(num1*num2)
                else:
                    stk.append(int(num1/num2))
            else: 
                stk.append(int(ch))
                
        return stk[0]


        