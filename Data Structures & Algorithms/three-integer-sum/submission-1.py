class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if a > 0:
                break
            
            if i > 0 and a == nums[i-1]:
                continue
            
            j = i+1
            k = len(nums) -1

            while j < k:
                threeSum = nums[j] + nums[k] + a
                if threeSum == 0:
                    res.append([a,nums[j],nums[k]])
                    j += 1
                    k -= 1

                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                elif threeSum < 0:
                    j += 1
                else:
                    k -= 1
                

        return res

        # res = []
        # for i in range(len(nums)):
        #     for j in range(i+1 ,len(nums)):
        #         if 0 - (nums[i] + nums[j]) in nums[j+1:]:
        #             res.append([nums[i],nums[j],0 - (nums[i] + nums[j])])
        # print(res)