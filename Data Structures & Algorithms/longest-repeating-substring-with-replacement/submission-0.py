class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        mp = {}
        left = 0

        for i in range(len(s)):
            mp[s[i]] = 1 + mp.get(s[i],0)
            while (i-left+1) - max(mp.values()) > k:
                mp[s[left]] -= 1
                left += 1
            res = max(res,i-left+1)
        return res

        