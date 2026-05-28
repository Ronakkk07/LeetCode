class Solution:
    # Recursion solution, TC - O(2**N), SC - O(N)
    def function(self, index, nums, current, ans):
        if index == len(nums):
            ans.append(current[:])
            return
        current.append(nums[index])
        self.function(index + 1, nums, current, ans)
        current.pop()
        self.function(index + 1, nums, current, ans)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.function(0, nums, [], ans)
        return ans