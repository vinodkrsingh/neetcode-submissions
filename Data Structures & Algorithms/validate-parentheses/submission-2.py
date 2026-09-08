class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        opening = {
        '(': ')',
        '{': '}',
        '[': ']'}
        stck = []

        for i in s:
            print(i)
            if i in opening:
                stck.append(i)
            elif not stck:
                return False
            else:
                if opening[stck.pop()] != i:
                    return False
        return False if stck else True
        

        