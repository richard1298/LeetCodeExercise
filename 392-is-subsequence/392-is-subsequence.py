class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j  = 0, 0 
        while i <= len(t)-1 and j <= len(s)-1:
            if t[i] == s[j]:
                i+=1
                j+=1
            else:
                i+=1
        if j>len(s)-1:
            return True
        else:
            return False