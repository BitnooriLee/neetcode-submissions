class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = [] 
        for token in tokens:
            if token in "+-*/": 
                if stk:
                    n2 = stk.pop()
                if stk:
                    n1 = stk.pop()
                if token == "+":
                    stk.append(n1+n2)
                elif token == "-":
                    stk.append(n1-n2)
                elif token == "*":
                    stk.append(n1*n2)
                else:
                    stk.append(int(n1/n2))
            else:
                    stk.append(int(token))
        return stk[0]