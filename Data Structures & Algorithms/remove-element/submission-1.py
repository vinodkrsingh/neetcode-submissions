class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        i = 0
        j = 0
        maxLen = len(nums) -1 
        while j <= maxLen:
            if nums[j] == val:
                j += 1
            elif nums[i] == val:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
                j += 1
            else:
                i += 1
                j += 1

        return i

        
        # k = 0
        # for i in range(len(nums)):
        #     if nums[i] != val:
        #         nums[k] = nums[i]
        #         k += 1
        
        # return k