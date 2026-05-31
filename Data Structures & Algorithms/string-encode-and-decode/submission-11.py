class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for st in strs:
            res += str(len(st))+ "#" + st
        return res
            

    def decode(self, s: str) -> List[str]:
        i = 0 
        res = []
        while(i < len(s)):
            start = i
            while(s[i].isdigit()):
                i+=1
            l = int(s[start:i])
            i+= 1 # remove # 
            res.append(s[i:i+l])
            i = i+l 
        return res 

            
                
