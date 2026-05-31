class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2: 
            return False
        stk = []

        for ch in s:
            if ch in "([{":
                stk.append(ch)
                print (stk)
            elif not stk:
                return False
            else:
                tmp = stk.pop()
                print(tmp)
                if (ch == ")" and tmp == "(") or (ch == "}" and tmp == "{") or (ch == "]" and tmp == "["):
                    continue
                else: 
                    return False
        return stk == []

                
        