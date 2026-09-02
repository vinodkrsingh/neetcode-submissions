class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        right = 0
        maxLen = 0
        deduset = set()

        while right < len(s):
            if s[right] not in deduset:
                maxLen = max(maxLen, right - left + 1)
                deduset.add(s[right])
                right += 1
            else:
                while s[right] in deduset:
                    deduset.remove(s[left])
                    left += 1
        return maxLen


        