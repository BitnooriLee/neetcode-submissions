class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = "+-*/"
        stk = []

        for i in range(len(tokens)):
            if tokens[i] not in op:
                stk.append(int(tokens[i]))
            elif tokens[i] == "+":
                n2 = stk.pop()
                n1 = stk.pop()
                stk.append(int(n1) + int(n2))
            elif tokens[i] == "-":
                n2 = stk.pop()
                n1 = stk.pop()
                stk.append(int(n1) - int(n2))
            elif tokens[i] == "*":
                n2 = stk.pop()
                n1 = stk.pop()
                stk.append(int(n1) * int(n2))
            else:
                n2 = stk.pop()
                n1 = stk.pop()
                stk.append(int(n1/n2))
                
        return stk[0]
