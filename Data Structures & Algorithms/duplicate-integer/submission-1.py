class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenSet = set()
        for i in nums:
            if i in seenSet:
                return True
            else:
                seenSet.add(i)
        return False

        # works only for positive values 
        # bitmask= 0
        # for num in nums:
        #     tracker = 1 << num

        #     if (bitmask & tracker) > 0:
        #         return True
        #     else:
        #         bitmask |= tracker
        # return False
        