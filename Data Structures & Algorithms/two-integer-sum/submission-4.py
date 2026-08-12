class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nmaps = {}

        for i, num in enumerate(nums):
            secRes = target - num
            if secRes not in nmaps:
                nmaps[num] = i
            else:
                return [nmaps.get(secRes), i]

        # for i in range(len(nums)):
        #     secTgt = target - nums[i]
        #     if secTgt in nums[i+1:]:
        #         return [i,nums[i+1:].index(secTgt) + i+1]
        