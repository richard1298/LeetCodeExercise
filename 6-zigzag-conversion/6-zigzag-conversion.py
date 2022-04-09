class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = ''
        if numRows == 1:
            return s
        else:
            for i in list(range(numRows)):
                temp = [s[t] for t in range(len(s)) if (t%(2*numRows-2) == i or t%(2*numRows-2) == (2*numRows-2-i)) ]
                temp = ''.join(temp)
                result += temp
            return result
        