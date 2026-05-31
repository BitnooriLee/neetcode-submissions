class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        res = ""
        def bt(res, op, cl):
            if op < cl or op > n:
                return 

            if len(res) == 2*n:
                output.append(res)
                return 
            
            bt(res+"(", op+1, cl)
            bt(res+")", op, cl+1)

        bt("", 0,0)

        return output