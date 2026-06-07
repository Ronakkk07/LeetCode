class Solution:
    def twoSum(self, nums: List[int], target: int):
        # TC - O(N), SC - O(N)
        mpp = {}
        for i in range(len(nums)):
            num = nums[i]
            more = target - num
            if more in mpp:
                return [mpp[more], i]
            mpp[num] = i
        return [-1, -1]
        # for index1,value1 in enumerate(nums):
        #     for index2,value2 in enumerate(nums):
        #         if index != index2:
        #             result = value1+value2
        #             if result == target:
        #                 return [index1, index2]

        # TC - O(n**2), SC - O(1)    
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         result = nums[i] + nums[j]
        #         if result == target:
        #             return [i, j]
                
