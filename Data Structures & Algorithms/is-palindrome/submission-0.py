class Solution:
    def isPalindrome(self, s: str) -> bool:
        output = ""
        for ch in s:
            if ch.isalnum():
                output += ch.lower()

        return output == output[::-1]
            