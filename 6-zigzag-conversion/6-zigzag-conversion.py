class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = ''
        if numRows == 1:
            return s
        else:
            for i in list(range(numRows)):
                for t in range(i,len(s),2*numRows - 2):
                    result += s[t]
                    if i >=1 and i <=numRows - 2 and t+2*numRows - 2 - 2*i <= len(s)-1:
                        result += s[t+2*numRows - 2 - 2*i]
        return result
            