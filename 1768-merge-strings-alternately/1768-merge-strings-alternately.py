class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        result = ''
        while i <= len(word1)-1 and j <= len(word2)-1:
            result += word1[i]
            result += word2[j]
            i+=1
            j+=1
        if i <= len(word1)-1:
            result+=word1[i:]
        if j <= len(word2)-1:
            result+=word2[j:]
        return result