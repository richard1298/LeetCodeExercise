class Solution:
    def tribonacci(self, n: int) -> int:
        self.rep = {}
        self.rep[0] = 0
        self.rep[1] = 1
        self.rep[2] = 1
        def fib_helper(n):
            if n <= 2:
                return self.rep[n]
            else:
                temp1 = 0
                temp2 = 0
                temp3 = 0
                if n-1 in self.rep:
                    temp1 = self.rep[n-1]
                else:
                    temp1 = fib_helper(n-1)
                    self.rep[n-1] = temp1
                    
                if n-2 in self.rep:
                    temp2 = self.rep[n-2]
                else:
                    temp2 = fib_helper(n-2)
                    self.rep[n-2] = temp2
                    
                if n-3 in self.rep:
                    temp3 = self.rep[n-3]
                else:
                    temp3 = fib_helper(n-3)
                    self.rep[n-3] = temp3
                result = temp1 + temp2 + temp3
                self.rep[n] = result
                return result
        return fib_helper(n)