class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for i in points:
            dist = (i[0]**2) + (i[1]**2)
            minHeap.append([dist,i[0],i[1]])
        
        heapq.heapify(minHeap)
        res = []
        while k > 0:
            i = heapq.heappop(minHeap)
            res.append([i[1],i[2]])
            k -= 1
        return res
        