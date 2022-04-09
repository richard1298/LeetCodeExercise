class Solution:
    def reverse(self, x: int) -> int:
        if x >=0:
            sign = 1
        else:
            sign = -1
        x = abs(x)
        digits = len(str(abs(x)))
        #print('It is a ',digits,'- digit number')
        result = 0
        for i in list(range(digits,0,-1)):
            a_i = x//10**(i-1)
            x = x - a_i * 10**(i-1)
            result += a_i * 10**(digits - i)
        result *= sign
        
        if (x //2**31 >=1 or x //2**31<-1) or (result //2**31 >=1 or result //2**31<-1):
            return 0
        else:
            return result
    