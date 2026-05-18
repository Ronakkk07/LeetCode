class Solution:
    def fib(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 0:
            return 0
        ans = self.fib(n-1) + self.fib(n-2)
        return ans 