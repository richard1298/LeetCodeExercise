class Solution:
    def minSwaps(self, s: str) -> int:
        lks=[]
        for x in s:
            if len(lks)==0:
                lks.append(x)
            elif lks[-1]=='[' and x==']':
                lks.pop()
            else:
                lks.append(x)
        k=len(lks)//2 + 1
        return k//2