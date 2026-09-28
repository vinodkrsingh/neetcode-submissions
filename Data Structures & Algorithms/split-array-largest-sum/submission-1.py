class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def currSplit(mid):
            currSum = 0
            currSplt = 1

            for n in nums:
                currSum = currSum + n
                if currSum > mid:
                    currSum = n
                    currSplt += 1
            return currSplt

        l = max(nums)
        r = sum(nums)
        res = r

        while l <= r:
            mid  = (l+r) // 2

            if currSplit(mid) <= k:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res

        