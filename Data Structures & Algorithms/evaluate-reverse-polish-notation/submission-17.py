class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for ch in tokens:
            if ch in "+-/*":
                if len(stk) > 1:
                    n2 = stk.pop()
                    n1 = stk.pop()
                    if ch == "+":
                        stk.append(n1+n2)
                    elif ch == "-":
                        stk.append(n1-n2)
                    elif ch == "*":
                        stk.append(n1*n2)
                    else:
                        stk.append(int(n1/n2))
                else:
                    return -1
                
            else:
                stk.append(int(ch))
        return stk[0]
                
        