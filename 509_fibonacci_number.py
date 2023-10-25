class Solution:
    def fib(self, n: int) -> int:
        if n > 2:
            return self.fib(n-1) + self.fib(n-2)
        elif n==0: 
            return 0
        else: 
            return 1