class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        freq = [0]*101
        res = []
        for num in nums:
            freq[num] += 1
            if freq[num] <= k:
                res.append(num)
        return res
