class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''
        for i in range(len(s)):
            l = i-1
            r = i+1
            temp = s[i]
            while l >=0 and r <= len(s) - 1 and s[l]==s[r]:
                temp = s[l] + temp + s[r]
                l -= 1
                r += 1
            if len(temp) > len(result):
                result = temp



            if i+1 <= len(s)-1 and s[i] == s[i+1]:
                temp = s[i]+s[i+1]
                l = i-1
                r = i+2

                while l >=0 and r <=len(s) - 1 and s[l] == s[r]:
                    temp = s[l] + temp + s[l]
                    l -= 1
                    r += 1
            if len(temp) > len(result):
                result = temp

        return result