class Solution:
    def reverseWords(self, s: str) -> str:
        splt = s.split()
        print('converted list = ',splt)
        for counter,elem in enumerate(splt):
            #print('this string = ',elem)
            elem=list(elem)
            #print('converted string = ',elem)
            l, r = 0, len(elem)-1
            while l<=r:
                elem[l],elem[r] = elem[r],elem[l]
                l+=1
                r-=1
            elem = ''.join(elem)
            splt[counter]=elem
            #print('reversed string = ',elem)
        return ' '.join(splt)