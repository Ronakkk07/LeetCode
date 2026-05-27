class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == divisor:
            return 1
        if dividend == -2**31 and divisor == -1:
            return 2**31 -1
        if divisor == 1:
            return dividend
        sign = not((dividend >=0 and divisor < 0) or (dividend < 0 and divisor > 0))
        n = abs(dividend)
        d = abs(divisor)
        ans = 0
        while n >= d:
            count = 0
            while ( n >= (d<< (count + 1))):
                count += 1
            ans += (1<<count)
            n -= (d<<count)
        if ans == (1 << 31) and sign:
            return 2**31 - 1
        if ans == (1 << 31) and not sign:
            return -2**31

        return ans if sign else -1 * ans