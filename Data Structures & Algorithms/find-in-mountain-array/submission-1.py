class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length  = mountainArr.length()

        l = 1
        r = length - 2

        while l <= r:
            m = (l+r) // 2
            lval, mval, rval = mountainArr.get(m-1), mountainArr.get(m), mountainArr.get(m+1)
            if lval < mval < rval:
                l = m + 1
            elif lval > mval > rval:
                r = m -1
            else:
                break
        
        peak = m

        l = 0
        r = peak

        while l <= r:
            mid = (l+r)//2
            if mountainArr.get(mid) == target:
                return mid
            elif mountainArr.get(mid) > target:
                r = mid -1
            else:
                l = mid + 1
        
        l = peak
        r = length -1

        while l <= r:
            mid = (l+r)//2
            if mountainArr.get(mid) == target:
                return mid
            elif mountainArr.get(mid) > target:
                l = mid + 1
            else:
                r = mid -1
        return -1
        