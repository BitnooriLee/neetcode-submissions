class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 !=0:
            return False
        stk = []
        for i in range(len(s)):
            if s[i] in "({[":
                stk.append(s[i])
            elif s[i] in ")}]":
                if stk:
                    top = stk.pop()
                    if (top == "(" and s[i] == ")") or (top == "{" and s[i] == "}") or (top == "[" and s[i] == "]"):
                        continue
                return False
            else:
                return False

        return stk == []