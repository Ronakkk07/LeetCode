class Solution:
    # Recursion solution, TC - O(2**N), SC - O(N)
    # def function(self, index, nums, current, ans):
    #     if index == len(nums):
    #         ans.append(current[:])
    #         return
    #     current.append(nums[index])
    #     self.function(index + 1, nums, current, ans)
    #     current.pop()
    #     self.function(index + 1, nums, current, ans)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        # ans = []
        # self.function(0, nums, [], ans)
        # return ans

        # Bit Manipulation (PowerSet Technique)
        n = len(nums)
        ans = []
        count = (1<<n)
        for val in range(count):
            subset = []
            for i in range(n):
                if val & (1 << i):
                    subset.append(nums[i])
            ans.append(subset)
        return ans