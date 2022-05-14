class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        rep = list(range(len(s)+1))
        l, r = 0, len(rep)-1
        result = []
        for i in range(len(s)):
            if s[i]=='I':
                result.append(rep[l])
                l+=1
            else:
                result.append(rep[r])
                r-=1
        result.append(rep[l])
        return result

        