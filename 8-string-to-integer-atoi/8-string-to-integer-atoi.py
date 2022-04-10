class Solution:
    def myAtoi(self, s: str) -> int:
    #the following block returns the first none empty char's index in s if there is any
        def locate(mys):
            start = 0
            while len(mys)>0:
                if start >= len(mys):
                    #this means the whole string is empty; start = +infinity
                    start = None
                    break
                else:
                    #this means we need to move start pointer by 1
                    if mys[start] == ' ':
                        start += 1
                    else:
                        break
            if len(s) ==0:
                start = None
            return start 
        start = locate(s)
        result = 0
        sign = 1
        end = 0
    #     print("first nonemtpy char at index =",start,'located')

        if start != None:
            #Define Boolean variables: A is true if the first nonempty char is + or -
            #B is true if the first is numeric
            if s[start] == '+' or s[start] == '-':
                if s[start] == '-':
                    sign = -1
                start += 1
    #         print('adjusted start =',start)
    #         print('s =',s)
    #         print('start <=(len(s)-1)=',start <=(len(s)-1))
    #         print('s[start].isnumeric()=',s[start].isnumeric())
    #         print('s[start] =',s[start])
            if start <=(len(s)-1) and s[start].isnumeric():
                end = start
    #             print('initial end index =',end)
                while end <=len(s)-1:
                    if s[end].isnumeric():
                        end += 1
                    else:
                        break
    #             print('final start index =',start,'final end index =',end)
                result = sign * int(s[start:end])
        if result >= 0:
            return min(result, 2**31-1)
        else:
            return max(result, -2**31)