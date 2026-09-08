class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        s = []
        for i in range(len(arr)):
            s.append([abs(x-arr[i]),i])
        s.sort()
        res = []
        for i in range(k):
            res.append(arr[s[i][1]])
        return sorted(res)
