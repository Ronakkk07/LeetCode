class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        sum = 0
        for x in range(1,1000):
            diff = abs(n-x)
            bin(x)[2:]
            bin(n)[2:]
            operation = n & x
            if diff <= k and operation == 0:
                sum += x
        return sum