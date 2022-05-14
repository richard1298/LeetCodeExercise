class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.find(ch)
        seg1=word[0:idx+1]
        if idx < len(word)-1:
            seg2 = word[idx+1:]
        else:
            seg2 =''
        #print('seg1=',seg1)
        #print('seg2=',seg2)
        a = list(seg1)
        a.reverse()
        seg1 = ''.join(a)
        #print('reversed seg 1 =', seg1)
        return ''.join([seg1,seg2])
