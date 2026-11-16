class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 !=0:
            return False

        st = []
        "[" "(" "{"
        "]" ")" "}"

        for i in range(len(s)):
            if s[i] in "[({":
                st.append(s[i])
            else:
                if not st:
                    return False
                cur = st.pop()
                if cur == "[" and s[i] == "]" or cur == "{" and s[i] == "}" or cur == "(" and s[i] == ")":
                    continue
                else:
                    return False

        return False if st else True 
                

        
        