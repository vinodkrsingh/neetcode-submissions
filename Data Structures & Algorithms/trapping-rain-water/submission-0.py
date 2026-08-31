class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        water = 0
        lmax= 0
        rmax = 0

        while l< r:
            if height[l] < height[r]:
                lmax = max(lmax, height[l])
                water += lmax - height[l]
                l +=1
            else:
                rmax = max(rmax,height[r])
                water += rmax - height[r]
                r -= 1
        return water
                


# class Solution:
#     def trap(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         left, right = 0, len(height) - 1
#         ans = 0
#         left_max, right_max = 0, 0
#         while left < right:
#             if height[left] < height[right]:
#                 left_max = max(left_max, height[left])
#                 ans += left_max - height[left]
#                 left += 1
#             else:
#                 right_max = max(right_max, height[right])
#                 ans += right_max - height[right]
#                 right -= 1
#         return ans