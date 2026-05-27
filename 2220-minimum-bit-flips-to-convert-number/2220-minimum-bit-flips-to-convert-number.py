class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        num = start ^ goal
        count = 0
        for i in range(32):
            count += (num & 1)
            num >>= 1
        return count