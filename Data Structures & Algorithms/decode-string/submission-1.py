class Solution:
    def decodeString(self, s: str) -> str:
        stk = []

        for i in s:
            if i == ']':
                s = ''
                j = stk.pop()
                while j != '[':
                    s = j + s
                    j = stk.pop()   
                k = ''
                while stk and stk[-1].isdigit():
                    k = stk.pop() + k
                stk.append(s*int(k))
            else:
                stk.append(i)
        return ''.join(stk)