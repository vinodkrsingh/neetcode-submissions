class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(len(nums)):
            absNm = abs(nums[i])
            if 1 <= absNm <= len(nums):
                if nums[absNm - 1] > 0:
                    nums[absNm - 1] *= -1
                elif nums[absNm - 1] == 0:
                    nums[absNm - 1] = -1*abs(len(nums)+1)
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i +1 
        return len(nums)+1


        