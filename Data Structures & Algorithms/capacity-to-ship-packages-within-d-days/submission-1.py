class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        minCap = r
        def canCarry(mid):
            day = 1
            tempMid = mid
            for i in weights:
                tempMid -= i
                if tempMid < 0:
                    day += 1
                    tempMid = mid
                    tempMid -= i
            return day <= days 

        while l <= r:
            mid = (l+r)//2
            if canCarry(mid):
                minCap = min(minCap, mid)
                r = mid - 1
            else:
                l = mid + 1
        return minCap
         

                

        