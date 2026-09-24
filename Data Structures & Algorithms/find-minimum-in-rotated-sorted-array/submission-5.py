class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        mn = max(nums)

        while l<=r:
            mid = (l+r)//2
            if nums[mid] < mn:
                mn =  nums[mid]
            elif nums[mid] >= nums[l] and nums[l] > nums[r]:
                l = mid+1
            else:
                r = mid - 1
        return mn

        