class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <=1:
            return [strs]
        
        dictMap = {}

        for i in range(len(strs)):
            sortVal = ''.join(sorted(strs[i]))
            if sortVal not in dictMap:
                dictMap[sortVal] = [strs[i]]
            else:
                dictMap[sortVal].append(strs[i])

        return list(dictMap.values())



