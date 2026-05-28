class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Brute Force - TC - O(N), SC - O(N)
        # count = {}
        # for num in nums:
        #     if num in count:
        #         count[num] += 1
        #     else:
        #         count[num] = 1
        # for key,value in count.items():
        #     if value == 1:
        #         return key
        # return -1

        # XOR solution, TC - O(N), SC - O(1)
        XOR = 0
        for num in nums:
            XOR ^= num
        return XOR