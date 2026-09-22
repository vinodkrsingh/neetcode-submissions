class Solution:
    def simplifyPath(self, path: str) -> str:

        stk = []
        arr = path.split('/')
        print(arr)
        for portion in arr:
            if portion == '..':
                if stk:
                    stk.pop()
            elif portion == '.' or portion == '':
                continue
            else:
                stk.append(portion)
        return '/'+'/'.join(stk)
