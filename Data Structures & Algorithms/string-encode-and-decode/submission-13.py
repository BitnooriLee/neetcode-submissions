class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for st in strs:
            l = len(st)
            tmp = str(l) + "@" + st 
            output += tmp    
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0 
        while(i<len(s)):
            j = i
            while(s[j]!="@"):
                j+=1
            l = int(s[i:j])
            output.append(s[j+1:j+l+1])
            i = j+l+1   
             
        return output
                
