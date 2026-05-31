class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = []
        for ch in s:
            if ch.isalpha() or ch.isalnum():
                tmp.append(ch.lower())
        half = len(tmp)//2
        for i in range(0,half):
            if tmp[i] != tmp[len(tmp)-i-1]:
                return False
        return True 
            
        