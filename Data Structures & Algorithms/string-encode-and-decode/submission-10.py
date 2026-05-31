class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for st in strs:
            res += str(len(st))+"%"+ st 
        print(res)
        return res 
            

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 
        while(i<len(s)):
            start = i
            while(i<len(s) and s[i].isdigit()):
                i+=1 
            length = int(s[start:i])
            i += 1
            res.append(s[i:i+length])
            i += length
                

        return res

