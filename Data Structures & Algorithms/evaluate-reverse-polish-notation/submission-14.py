class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for t in tokens:
            if t in "+-*/":
                if stk:
                    n2 = stk.pop()
                else: return -1 
                if stk:
                    n1 = stk.pop()
                else: return -1
                
                if t == "+":
                    stk.append(n1+n2)
                elif t == "-":
                    stk.append(n1-n2)
                elif t == "*":
                    stk.append(n1*n2)
                else:
                    stk.append(int(n1/n2))
            else:
                stk.append(int(t))

        return stk[0]
                
        