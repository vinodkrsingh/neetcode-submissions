class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lenNums = len(nums)
        if lenNums <= 1:
            return lenNums
        
        left = 0
        right = 1
        count = 1

        while right <= lenNums -1:
            if nums[left] != nums[right]:
                nums[count] = nums[right]
                count += 1
                left = right
            right += 1
        
        return count



        