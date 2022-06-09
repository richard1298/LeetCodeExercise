class Solution:
    def climbStairs(self, n: int) -> int:
        self.rep={}
        self.rep[1]=1
        self.rep[2]=2
        def clib_helper(n):
            if n == 1 or n ==2:
                return self.rep[n]
            else:
                temp1, temp2 = 0,0
                if n-1 in self.rep:
                    temp1 = self.rep[n-1]
                else:
                    temp1 = clib_helper(n-1)
                if n-2 in self.rep:
                    temp2 = self.rep[n-2]
                else:
                    temp2 = clib_helper(n-2)
                self.rep[n]=temp1+temp2
                return self.rep[n]
        return clib_helper(n)    
        