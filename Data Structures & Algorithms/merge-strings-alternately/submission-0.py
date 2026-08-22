class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0 
        w1len = len(word1) -1
        w2len = len(word2) -1 
        out = ""

        while i <= w1len and  i <= w2len:
            out += word1[i] + word2[i]
            i+=1
        
        if i == w1len +1:
            out += word2[i:]
        else:
            out += word1[i:]
        return out


        