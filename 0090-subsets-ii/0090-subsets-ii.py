class Solution:
    def function(self, index, current, nums, ans):
        if index == len(nums):
            ans.append(current[:])
            return
        current.append(nums[index])
        self.function(index + 1, current, nums, ans)
        current.pop()
        
        next_index = index + 1
        while next_index < len(nums) and nums[next_index] == nums[index]:
            next_index += 1
        self.function(next_index, current, nums, ans)
 
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        self.function(0, [], nums, ans)
        return ans