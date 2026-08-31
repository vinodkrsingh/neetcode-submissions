class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        left = 0
        right = len(people) -1
        count = 0

        while left <= right:
            count += 1
            currLim = people[left] + people[right]
            if currLim <= limit and left <= right:
                left += 1
            right -= 1

        return count
                

        