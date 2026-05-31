class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_updated = ""
        for ch in s:
            if ch.isalnum():
                s_updated += ch.lower()
        return s_updated == s_updated[::-1]

        