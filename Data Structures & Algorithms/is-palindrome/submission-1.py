class Solution:
    def isAlpNum(self, c):
        return (ord('a') <= ord(c.lower()) <= ord('z')) or (ord('0') <= ord(c) <= ord('9'))
    def isPalindrome(self, s: str) -> bool:
        i = 0 
        r = len(s) -1
        while i < r:
            if self.isAlpNum(s[i]) and self.isAlpNum(s[r]) and s[i].lower() == s[r].lower():
                i += 1
                r -= 1
            elif self.isAlpNum(s[i]) and self.isAlpNum(s[r]) and s[i].lower() != s[r].lower():
                return False
            else:
                if self.isAlpNum(s[r]) == False:
                    r -= 1
                if self.isAlpNum(s[i]) == False:
                    i += 1
        return True
        