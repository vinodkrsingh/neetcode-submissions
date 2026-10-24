class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        
        heapq.heapify(stones)

        while len(stones)>1:
            fstNbr = heapq.heappop(stones)
            scndNbr = heapq.heappop(stones)
            # print()
            heapq.heappush(stones,fstNbr-scndNbr)
        return -stones[0]