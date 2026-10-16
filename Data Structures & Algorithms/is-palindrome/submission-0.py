class Solution:
    def isPalindrome(self, s: str) -> bool:
        modified = ""
        for i in s:
            if i.isalnum():
                modified += i.lower()
        left = 0
        right= len(modified)-1

        while left < right:
            if modified[left] != modified[right]:
                return False
            left += 1
            right -= 1

        return True