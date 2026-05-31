class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res,part = [], []
        
        def dfs(i): #current position
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                tmp = s[i:j+1]
                if tmp == tmp[::-1]:
                    part.append(tmp)
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return res
            
        
        