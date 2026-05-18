class Solution:
    def fib(self, n: int) -> int:
        # TC - O(2**n), SC - O(n)
        # if n == 1:
        #     return 1
        # if n == 0:
        #     return 0
        # if n <= 1:
        #     return n
        # return self.fib(n-1) + self.fib(n-2) 

        #  Dynamic Programming Tabulation TC - O(n), SC - O(n)
        if n <= 1:
            return n
        f = [0] * (n+1)
        f[0] = 0
        f[1] = 1

        for i in range(2, n+1):
            f[i] = f[i-1] + f[i-2]
        
        return f[n]
