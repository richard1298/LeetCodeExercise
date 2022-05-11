class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        i = 0
        result = 0
        if len(s)<=2:
            result = 0
        else:
            while i+2<=len(s)-1:
                #print('section = ',s[i:i+3])
                if len(set(s[i:i+3])) == len(s[i:i+3]):
                    result += 1
                i+=1
        return result
