class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        dic = {"2": "abc", 
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"
                }

         #combination  
        output = []
        n = len(digits)

        def dfs(path,i):
            if i == n:
                output.append(path)
                return  
            for j in range(len(dic[digits[i]])):
                dfs(path+dic[digits[i]][j], i+1)     
        
        dfs("",0)
        
        return output 
        