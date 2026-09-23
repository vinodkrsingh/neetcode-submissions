class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x // 2

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