class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dct = {0:1}
        res = 0
        sum = 0

        for i in nums:
            sum += i
            dif = sum - k
            if dif in dct:
                res += dct.get(dif,0)
            dct[sum] = 1 + dct.get(sum,0)
        return res


        