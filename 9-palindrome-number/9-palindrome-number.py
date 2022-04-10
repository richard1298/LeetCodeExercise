class Solution:
    def isPalindrome(self, x: int) -> bool:
        import math
        if x< 0:
            return False
        else:
            if x<=9:
                return True
            else:
                #this line of code computes the number of digits for the positive integer
                digits = math.floor(math.log10(x))+1
                l = digits
                r = 1
                result = True
                #print('digits =',digits)
                while l >= r:
                    first = x//(10**(l-1))
                    last = x%10
                    #print('first =',first,'last =',last)
                    if first == last:
                        #print("##first = last!")
                        x = (x - last - first*10**(l-1))/10
                        l -= 2
                        #print('updated x =',x)
                        #print('updated l =',l,'updated r =',r)
                    else:
                        result = False
                        break
                return result
        
        