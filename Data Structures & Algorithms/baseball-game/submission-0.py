class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stck = []
        out = 0
        print(operations)
        for i in operations:
            if i == '+':
                b = stck.pop()
                a = stck.pop()
                sm = a+b
                stck.append(a)
                stck.append(b)
                stck.append(sm)
            elif i == 'C':
                stck.pop()
            elif i == 'D':
                a = stck.pop()
                dbl = 2*a
                stck.append(a)
                stck.append(dbl)
            else:
                stck.append(int(i))
        
        for i in stck:
            out += i
        return out
        







