class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # TC - O(n), SC - O(n)
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return num
        #     seen.add(num)

        # slow and fast pointers TC - O(n), SC - O(1)
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow