class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = [] 

        for tk in tokens:
            if tk in '+-*/':
                tmp1 = stk.pop()
                tmp2 = stk.pop()
                if tk == '+':
                    re = tmp1 + tmp2
                elif tk == '-':
                    re = tmp2 - tmp1
                elif tk == '*':
                    re = tmp1*tmp2
                else:
                    re = int(tmp2/tmp1)
                stk.append(re)
            else:
                stk.append(int(tk))
        return stk[0]
        