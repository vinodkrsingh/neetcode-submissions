class Solution:
    def validPalindrome(self, s: str) -> bool:
        delCnt = 1
        l, r = 0, len(s)-1

        while l<r:
            # print(s[l],s[r])
            if s[l] != s[r]:
                skipL, skipR = s[l+1:r+1], s[l:r]
                if skipL != skipL[::-1] and skipR != skipR[::-1]:
                    return False
            l += 1
            r -= 1
        return True