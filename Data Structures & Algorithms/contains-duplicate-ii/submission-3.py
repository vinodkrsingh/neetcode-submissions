class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        st = {}
        j = 0
        while j < len(nums):
            # print(st,nums[j],j)
            if nums[j] in st:
                if j - st[nums[j]] <= k:
                    return True
                else:
                    st[nums[j]] = j
            else:
                st[nums[j]] = j
            j+=1
        return False