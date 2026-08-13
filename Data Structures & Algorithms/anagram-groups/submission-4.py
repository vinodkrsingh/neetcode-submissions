class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dicList = defaultdict(list)

        for s in strs:
            countArr = [0] * 26
            for c in s:
                countArr[ord(c) - ord('a')] += 1
            dicList[tuple(countArr)].append(s)
        
        return list(dicList.values())


        # if len(strs) <=1:
        #     return [strs]
        
        # dictMap = {}

        # for i in range(len(strs)):
        #     sortVal = ''.join(sorted(strs[i]))
        #     if sortVal not in dictMap:
        #         dictMap[sortVal] = [strs[i]]
        #     else:
        #         dictMap[sortVal].append(strs[i])

        # return list(dictMap.values())



