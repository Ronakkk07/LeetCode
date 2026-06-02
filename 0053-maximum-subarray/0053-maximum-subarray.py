class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # TC - O(n**2), Sc - O(1) - TLE 10**5 constraint
        # max_sum = float('-inf')
        # for  i in range(len(nums)):
        #     current_sum = 0
        #     for j in range(i, len(nums)):
        #         current_sum += nums[j]
        #         if current_sum > max_sum:
        #             max_sum = current_sum
        # return max_sum

        # TC - O(n), SC - O(1)
        max_sum = float('-inf')
        current_sum = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            if current_sum > max_sum:
                max_sum = current_sum
            if current_sum < 0:
                current_sum = 0
        return max_sum