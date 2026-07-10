class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True

        text = "".join(char for char in s if char.isalnum()).lower()

        i = 0
        j = len(text) - 1

        while i <= j:
            if text[i] != text[j]:
                return False
            i += 1
            j -= 1
        
        return True