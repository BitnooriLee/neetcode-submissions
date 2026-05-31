class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        if len(s)%2:
            return False

        for ch in s:
            if ch in '({[':
                stk.append(ch)
            elif stk:
                tmp = stk.pop()
                if (ch == ')' and tmp == "(") or (ch == '}' and tmp == "{") or (ch == ']' and tmp == "[") :
                    continue

                else: return False
            else:
                return False
        return not stk
        
        