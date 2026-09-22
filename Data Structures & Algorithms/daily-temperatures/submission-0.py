class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stck = []
        res = [0]* len(temperatures)

        for i, num in enumerate(temperatures):
            while stck and num > stck[-1][0]:
                stkVal = stck.pop()
                res[stkVal[1]] = i-stkVal[1]
            stck.append((num,i))
        return res


        