class Solution:
    def minWindow(self, s: str, t: str) -> str:

        have = 0
        left = 0
        needDict = {}
        haveDict = {}
        res = [-1, -1]
        resLen = len(s) + 1

        for i in t:
            needDict[i] = 1+needDict.get(i,0)
        need = len(needDict)

        for r in range(len(s)):
            # print(s[r])
            if s[r] in needDict:
                haveDict[s[r]] = 1+haveDict.get(s[r],0)
                if haveDict[s[r]] == needDict[s[r]]:
                    have += 1
                    # print(needDict,haveDict,have)
            # print(need,have,r,left,resLen)
            
            while need == have: 
                # print(need,have,r,left,resLen)
                if (r - left + 1) < resLen:
                    res = [left,r]
                    resLen = r - left + 1
                if s[left] in haveDict:
                    haveDict[s[left]] -= 1
                    if haveDict[s[left]] < needDict[s[left]]:
                        have = have - 1
                    # print(haveDict,needDict,have)
                left += 1
        return s[res[0]:res[1]+1] if resLen != len(s) + 1 else ''




        