class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'2': "abc", '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs','8':'tuv','9':'wxyz'}
        res = []
        path = []
        if not digits:
            return []
        def backtrack(i):

            if i == len(digits):
                res.append("".join(path)) #join은 읽기만함..? 
                return

            for ch in dic[digits[i]]:
                path.append(ch)
                backtrack(i+1)
                path.pop()

        backtrack(0)
        return res 

        
        