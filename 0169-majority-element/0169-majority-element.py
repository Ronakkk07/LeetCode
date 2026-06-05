class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # TC - O(n), SC - O(n)
        n = len(nums)
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        for num, count in freq.items():
            if count > n//2:
                return num
        return -1