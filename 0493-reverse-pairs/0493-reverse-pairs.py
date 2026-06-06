class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.merge_sort(nums, 0, len(nums) - 1)
    def merge_sort(self, nums, low, high):
        if low >= high:
            return 0
        mid = (low + high) // 2
        cnt = 0
        cnt += self.merge_sort(nums, low, mid)
        cnt += self.merge_sort(nums, mid + 1, high)
        cnt += self.count_pairs(nums, low, mid, high)
        self.merge(nums, low, mid, high)
        return cnt
    def count_pairs(self, nums, low, mid, high):
        right = mid + 1
        cnt = 0
        for i in range(low, mid+1):
            while right <= high and nums[i] > 2 * nums[right]:
                right += 1
            cnt += right - (mid + 1)
        return cnt
    def merge(self, nums, low, mid, high):
        temp = []
        left, right = low, mid + 1
        while left <= mid and right <= high:
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1
        while left <= mid:
            temp.append(nums[left])
            left += 1
        while right <= high:
            temp.append(nums[right])
            right += 1
        nums[low:high+1] = temp
        
        # TLE TC - O(n**2), SC - O(1)
        # n = len(nums)
        # cnt = 0
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] > 2*nums[j]:
        #             cnt += 1
        # return cnt