class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Moore's Voting Algorithm TC - O(n), SC - O(1)
        n = len(nums)
        element = 0
        count = 0
        for num in nums:
            if count == 0:
                count = 1
                element = num
            elif element == num:
                count += 1
            else:
                count -= 1
        cnt = nums.count(element)
        if cnt > n//2:
            return element
        return -1

        # TC - O(n), SC - O(n)
        # n = len(nums)
        # freq = {}
        # for num in nums:
        #     if num in freq:
        #         freq[num] += 1
        #     else:
        #         freq[num] = 1
        # for num, count in freq.items():
        #     if count > n//2:
        #         return num
        # return -1
