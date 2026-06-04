class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        arr = [0] * (m+n)
        i = j = index = 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                arr[index] = nums1[i]
                i += 1
            else:
                arr[index] = nums2[j]
                j+=1
            index += 1
        while i < m:
            arr[index] = nums1[i]
            i += 1
            index+= 1
        while j < n:
            arr[index] = nums2[j]
            j += 1
            index += 1
        for r in range(m+n):
            nums1[r] = arr[r]