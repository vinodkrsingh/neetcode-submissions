class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        l = 0
        for r in range(len(nums)):
            # print(window, r , l,r - l)
            if r - l > k:
                window.remove(nums[l])
                l += 1
            if nums[r] in window:
                return True
            window.add(nums[r])

        return False



        # st = {}
        # j = 0
        # while j < len(nums):
        #     if nums[j] in st:
        #         if j - st[nums[j]] <= k:
        #             return True
        #         else:
        #             st[nums[j]] = j
        #     else:
        #         st[nums[j]] = j
        #     j+=1
        # return False