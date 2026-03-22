class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''
        for char in s:
            if char.isalpha():
                new_s += char.lower()
            elif char.isnumeric():
                new_s += char
            
        return new_s == new_s[::-1]