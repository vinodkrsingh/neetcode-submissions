class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) -1 
        if target > nums[r]:
            return r + 1
        elif target < nums[l]:
            return 0
        
        while l <= r:
            print(l,r)
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid +1
            else:
                r = mid -1
        return l
        