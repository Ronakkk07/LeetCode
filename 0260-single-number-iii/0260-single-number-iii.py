class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # TC-O(N) Traversing the array twice results in O(2*N) TC, SC - O(1)
        n = len(nums)
        XOR = 0
        for num in nums:
            XOR ^= num
        rightmost = (XOR & (XOR-1)) ^ XOR
        b1,b2 = 0,0
        for i in range(n):
            if nums[i] & rightmost:
                b1 = b1^nums[i]
            else:
                b2 = b2^nums[i]
        return [b1,b2]