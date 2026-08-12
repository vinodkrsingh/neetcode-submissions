class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longStr = ''
        for i in range(len(strs[0])):
            for j in strs[1:]:
                if len(j) <= i or strs[0][i] != j[i]:
                    return longStr
            longStr += (strs[0][i])
        return longStr

        
        