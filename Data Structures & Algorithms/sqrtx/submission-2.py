class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        r = x // 2
        if x == 0:
            return 0

        while l <= r:
            mid = (l+r)//2
            midsqt = mid**2
            if midsqt == x:
                return mid
            elif midsqt < x:
                l = mid + 1
            else:
                r = mid - 1
        return 1 if r == 0 else r  