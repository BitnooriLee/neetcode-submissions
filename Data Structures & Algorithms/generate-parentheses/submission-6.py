class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        def bt(o,c,tmp):
            if o > n or c > n or o < c:
                return 
            if len(tmp) == 2*n:
                output.append("".join(tmp))
                return 
            tmp.append("(")
            bt(o+1,c,tmp)
            tmp.pop()
            tmp.append(")")
            bt(o,c+1,tmp)
            tmp.pop()

        bt(0,0,[])

        return output