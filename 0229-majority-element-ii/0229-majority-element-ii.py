from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mpp = defaultdict(int)
        result = []
        for num in nums:
            mpp[num] += 1
        for num, count in mpp.items():
            if count > n//3:
                result.append(num)
        return result
             

        