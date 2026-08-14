class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cntDic = defaultdict(int)
        mjrEl = len(nums)//2
        for num in nums:
            cntDic[num] = 1 + cntDic.get(num,0)
        
        for i in cntDic:
            if cntDic[i] >= mjrEl:
                return i
        
        