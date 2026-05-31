class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 == 1:
            return False 
        
        sk = []
        for ch in s:
            if ch in ")}]":
                if len(sk) < 1:
                    return False
                pair = sk[-1]
                if ch == ")" and pair == '(' or ch == '}' and pair == '{' or ch == ']' and pair == '[':
                    sk.pop()
                    continue
                else:
                    return False 
            else:
                sk.append(ch)
        return True if len(sk) == 0 else False
        
                    

            

        
#two pointer : {}()() x 
# stack 