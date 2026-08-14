class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = count = 0

        for num in nums:
            if count == 0:
                res = num
            count += (1 if res == num else -1)
        return res






        # cntDic = defaultdict(int)
        # mjrEl = len(nums)//2
        # for num in nums:
        #     cntDic[num] = 1 + cntDic.get(num,0)
        
        # for i in cntDic:
        #     if cntDic[i] >= mjrEl:
        #         return i
        
        