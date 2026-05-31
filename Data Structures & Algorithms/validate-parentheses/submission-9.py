class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 == 1:
            return False 
        
        sk = []
        for ch in s:
            if ch in ")}]":
                if not sk: return False
                pair = sk[-1]
                if ch == ")" and pair == '(' or ch == '}' and pair == '{' or ch == ']' and pair == '[':
                    sk.pop()
                    continue
                else:
                    return False 
            else:
                sk.append(ch)
        return not sk
        
                    

            

        
#two pointer : {}()() x 
# stack 