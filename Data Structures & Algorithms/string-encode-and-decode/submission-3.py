class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for i in strs:
            result += str(len(i)) + "#" + i
        return result

    def decode(self, s: str) -> List[str]:

        i = 0
        res = []
        print(s)

        while i<len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            # print(length)
            j = i + len(str(length)) +1  + length
            res.append(s[i + len(str(length)) +1:j])
            i = j
        return res

