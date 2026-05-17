class Solution:
#     Time and Space Complexity
#     Time Complexity: O(log n), due to modular exponentiation for computing 5^ceil(n/2) and 4^floor(n/2).
#     Space Complexity: O(1), as we use only a constant number of variables; no extra space proportional to n is required.
    MOD = 10**9 + 7
    def modPow(self, base, exp):
        result = 1
        base %= self.MOD
        while exp > 0:
            if  exp % 2 == 1:
                result = (result * base) % self.MOD
            base = (base * base) % self.MOD
            exp //= 2
        return result

    # def is_prime(self, n):
    #     if n < 2:
    #         return False
    #     for index in range(2, int(n**0.5) + 1):
    #         if n % index == 0:
    #             return False
    #     return True

    def countGoodNumbers(self, n: int) -> int:
        # MOD = 10**9 + 7
        # i = 0
        # ans = 1

        # while i < n:
        #     if  i % 2 == 1:
        #         options = 0
        #         for j in range(10):
        #             if self.is_prime(j):
        #                 options += 1
        #         ans = (ans*options) % MOD
        #     else:
        #         count = 0
        #         for j in range(10):
        #             if j % 2 == 0:
        #                 count += 1
        #         ans = (ans*count) % MOD
        #     i += 1
        # return ans # TLE ofc

        even_positions = (n+1)//2
        odd_positions = n // 2

        res = (self.modPow(5, even_positions) * self.modPow(4, odd_positions)) % self.MOD
        return res
