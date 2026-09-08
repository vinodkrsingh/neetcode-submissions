class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mins = len(nums) +1 

        lft = 0 
        # rgt = 0
        tempSum = 0

        for i in range(len(nums)):
            tempSum += nums[i]
            while tempSum >= target:
                mins = min(mins, i - lft + 1)
                tempSum -= nums[lft]
                lft += 1
        return 0 if mins == (len(nums) + 1) else mins

        
        # while rgt < len(nums) and lft <= rgt:
        #     print(tempSum,rgt,lft)

        #     if tempSum >= target:
        #         mins = min(mins, rgt - lft + 1)
        #         tempSum -= nums[lft]
        #         lft += 1
        #     else:
        #         if rgt == len(nums): break
        #         rgt += 1
        #         tempSum += nums[rgt]
                
        # return 0 if mins == (len(nums) + 1) else mins