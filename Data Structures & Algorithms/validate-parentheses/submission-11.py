class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 !=0:
            return False

        op = "([{"
        cs = "}])"
        stk = [] 

        for ch in s:
            if ch in "([{":
                stk.append(ch)
            elif ch in "}])":
                if not stk:
                    return False
                st = stk.pop()
                if (st == "(" and ch == ")") or (st == "[" and ch == "]") or (st=="{" and ch=="}"):
                    continue
                else:
                    return False
        return True if not stk else False
                

        
        