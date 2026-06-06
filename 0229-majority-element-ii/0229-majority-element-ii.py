from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # mpp = defaultdict(int)
        # result = []
        # for num in nums:
        #     mpp[num] += 1
        # for num, count in mpp.items():
        #     if count > n//3:
        #         result.append(num)
        # return result

        # Moore's Voting Algorithm
        n = len(nums)
        count1, count2 = 0,0
        element1, element2 = float('-inf'), float('-inf')
        for num in nums:
            if count1 == 0 and element2 != num:
                count1 += 1
                element1 = num
            elif count2 == 0 and element1 != num:
                count2 += 1
                element2 = num
            elif num == element1:
                count1 += 1
            elif num == element2:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        count1, count2 = 0,0
        for num in nums:
            if num == element1:
                count1 += 1
            if num == element2:
                count2 += 1
        mini = n//3+1
        result = []
        if count1 >= mini:
            result.append(element1)
        if count2 >= mini and element1 != element2:
            result.append(element2)
        return result
             

        