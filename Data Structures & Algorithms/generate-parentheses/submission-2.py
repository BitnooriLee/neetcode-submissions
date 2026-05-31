class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []

        def backtracking(path,op,cs):
            if len(path) >= 2*n:
                output.append(path)

            if op < n:
                backtracking(path+"(", op+1, cs)
            if cs < op:
                backtracking(path+")", op, cs+1)

        backtracking("",0,0)
        return output
        