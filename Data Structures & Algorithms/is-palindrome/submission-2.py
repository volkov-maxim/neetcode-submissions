class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_purified = "".join(char.lower() for char in s if char.isalnum())
        return s_purified == s_purified[::-1]
