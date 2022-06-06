class Solution:
    def fib(self, n: int) -> int:
        self.rep = {}
        self.rep[0]=0
        self.rep[1]=1
        def fib_helper(n):
            result = 0
            if n in self.rep:
                result = self.rep[n]
            else:
                result = fib_helper(n-1)+fib_helper(n-2)
                self.rep[n] = result
            return result
        return fib_helper(n)