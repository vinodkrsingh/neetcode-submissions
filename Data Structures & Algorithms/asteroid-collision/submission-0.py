class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stk = []

        for i in asteroids:
            # print(stk)
            while stk and stk[-1] > 0 and i < 0:
                winner = stk[-1] + i
                # print(winner)
                if winner < 0:
                    stk.pop()
                elif winner > 0:
                    i = 0
                else:
                    i = 0
                    stk.pop()
                # print(stk)
            if i != 0:
                stk.append(i)
        return stk


        
        