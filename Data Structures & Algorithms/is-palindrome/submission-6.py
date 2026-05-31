class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        ss = ""
        for ch in s:
            if ch.isalnum():
                ss += ch.lower()
        i,j = 0, len(ss)-1
        while(i<j):
            if ss[i] != ss[j]:
                return False
            i += 1
            j -= 1

        return True


        