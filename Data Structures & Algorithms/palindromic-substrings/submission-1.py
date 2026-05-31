class Solution:
    def countSubstrings(self, s: str) -> int:
        output = 0 
        for l in range(len(s)):
            for r in range(l,len(s)):
                tmp = s[l:r+1]
                if tmp == tmp[::-1]:
                    output += 1
        return output
        