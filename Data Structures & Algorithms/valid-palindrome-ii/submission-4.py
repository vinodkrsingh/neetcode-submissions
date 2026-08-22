class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check_palindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            
            return True

        i = 0
        j = len(s) - 1
        while i < j:
            # Found a mismatched pair - try both deletions
            if s[i] != s[j]:
                return check_palindrome(s, i, j - 1) or check_palindrome(s, i + 1, j)
            i += 1
            j -= 1
        
        return True
        # delCnt = 1
        # l, r = 0, len(s)-1

        # while l<r:
        #     # print(s[l],s[r])
        #     if s[l] != s[r]:
        #         skipL, skipR = s[l+1:r+1], s[l:r]
        #         if skipL != skipL[::-1] and skipR != skipR[::-1]:
        #             return False
        #     l += 1
        #     r -= 1
        # return True