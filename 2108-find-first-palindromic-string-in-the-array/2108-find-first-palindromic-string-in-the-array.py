class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        output=''
        for elem in words:
            i, j = 0, len(elem)-1
            result = True
            while i<=j:
                if elem[i]==elem[j]:
                    i+=1
                    j-=1
                else:
                    result = False
                    break
            if result == True:
                output = elem
                break
        return output        