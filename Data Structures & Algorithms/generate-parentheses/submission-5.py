class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        res = []
        self.n = n
        def bt(op, cl):
            if op < cl or op > self.n:
                return 

            if len(res) == 2*n:
                output.append("".join(res))
                return 
            res.append("(")
            bt(op+1, cl)
            res.pop()
            res.append(")")
            bt(op, cl+1)
            res.pop()

        bt(0,0)

        return output