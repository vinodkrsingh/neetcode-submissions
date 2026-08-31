class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        currentWater = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            currentWater = min(heights[left], heights[right]) * (right - left)
            maxWater = max(maxWater, currentWater)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return maxWater
            
        