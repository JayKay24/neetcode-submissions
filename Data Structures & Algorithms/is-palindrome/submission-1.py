class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        left, right = 0, n - 1

        while left <= right:
            while left < n and not s[left].isdigit() and not s[left].isalpha():
                left += 1
            while right >= 0 and not s[right].isdigit() and not s[right].isalpha():
                right -= 1
            
            if left < n and right >= 0 and s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True