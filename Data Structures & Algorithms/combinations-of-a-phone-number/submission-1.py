class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dic = { "2":"abc", "3":"def", "4":"ghi", "5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        output = []

        def dfs(path, i):
            if i >= len(digits):
                output.append(path)
                return
            for ch in dic[digits[i]]:
                dfs(path+ch, i+1)

        dfs("",0)

        return output


        