class Solution:
    def myPow(self, x: float, n: int) -> float:
        #Optimal Iterative Approach, TC - O(log(n)), SC - O(1) - Iterative soln
        # if n == 0 or x == 1.0:
        #     return 1
        # if n < 0:
        #     x = 1/x
        #     n = -n
        # ans = 1
        # while n > 0:
        #     if n % 2 == 1:
        #         ans *= x
        #     x *= x
        #     n = n//2
        # return ans

        #Recursive Approach, TC - O(logN), SC - O(logN) (Recursive stack space is used)
        if n == 0:
            return 1
        if n < 0:
            x = 1/x
            n = -n
        if n % 2 == 1:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n//2)
