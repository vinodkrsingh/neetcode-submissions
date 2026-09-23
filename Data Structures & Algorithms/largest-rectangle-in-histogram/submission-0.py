class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        maxht = 0

        for i, h in enumerate(heights):
            mnInd = i
            while stk and h < stk[-1][0]:
                popedItem = stk.pop()
                ln = i-popedItem[1]
                maxht = max(maxht,popedItem[0]*ln)
                mnInd = popedItem[1]
            stk.append((h, mnInd))
        while stk:
            popedItem = stk.pop()
            ln = len(heights)-popedItem[1]
            maxht = max(maxht,popedItem[0]*ln)
        return maxht

            

        