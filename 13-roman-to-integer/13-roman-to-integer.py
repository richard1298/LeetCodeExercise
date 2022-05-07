class Solution:
    def romanToInt(self, s: str) -> int:
        j = 0
        result = 0
        SYMBOL={'M':1000,
                'CM':900,
                'D':500,
                'CD':400,
                'C':100,
                'XC':90,
                'L':50,
                'XL':40,
                'X':10,
                'IX':9,
                'V':5,
                'IV':4,
                'I':1}
        while j< len(s):
            if j<len(s)-1 and s[j:j+2] in SYMBOL:
                this_key = s[j:j+2]
                j += 2
                result += SYMBOL[this_key]
            else:
                result += SYMBOL[s[j]]
                j+= 1
        return result