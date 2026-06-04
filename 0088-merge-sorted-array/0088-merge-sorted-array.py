class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # TC - O(N+M), SC - O(N+M)
        # arr = [0] * (m+n)
        # i = j = index = 0
        # while i < m and j < n:
        #     if nums1[i] <= nums2[j]:
        #         arr[index] = nums1[i]
        #         i += 1
        #     else:
        #         arr[index] = nums2[j]
        #         j+=1
        #     index += 1
        # while i < m:
        #     arr[index] = nums1[i]
        #     i += 1
        #     index+= 1
        # while j < n:
        #     arr[index] = nums2[j]
        #     j += 1
        #     index += 1
        # for r in range(m+n):
        #     nums1[r] = arr[r]

        # Two pointers -> TC - O(min(N, M)) + O(NxlogN) + O(MxlogM) + O(N), SC - O(1)
        left = m-1
        right = 0
        while left >= 0 and right < n:
            if nums1[left] > nums2[right]:
                nums1[left], nums2[right] = nums2[right], nums1[left]
                left -= 1
                right += 1
            else:
                break
        nums1[:m] = sorted(nums1[:m])
        nums2.sort()
        for i in range(m, m + n):
            nums1[i] = nums2[i - m]

