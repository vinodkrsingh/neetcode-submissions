class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longStr = ''
        minlen= len(strs[0])

        for i in strs[1:]:
            minlen = min(minlen,len(i))

        for i in range(minlen):
            for j in strs[1:]:
                if strs[0][i] != j[i]:
                    return longStr
            longStr += (strs[0][i])
        return longStr

        
        