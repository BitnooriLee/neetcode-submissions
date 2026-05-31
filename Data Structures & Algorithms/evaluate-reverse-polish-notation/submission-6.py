class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = [] 
        for tk in tokens:
            if tk not in "+-*/":
                stk.append(int(tk))
            else:
                num2 = stk.pop()
                num1 = stk.pop()
                if tk == "+":
                    stk.append(num1+num2)
                elif tk == "-":
                    stk.append(num1-num2)
                elif tk == "*":
                    stk.append(num1*num2)
                else:
                    stk.append(int(num1/num2))
        return stk[0]

        
        