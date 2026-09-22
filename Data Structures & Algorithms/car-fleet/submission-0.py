class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = [[p, s] for p, s in zip(position, speed)]
        arr.sort(reverse = True)
        stk = []
        for i in arr:
            timeTaken  = (target - i[0])/i[1]
            if stk and stk[-1] >= timeTaken:
                pass
            else:
                stk.append(timeTaken)
        return len(stk)

        