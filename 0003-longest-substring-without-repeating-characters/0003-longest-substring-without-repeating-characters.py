class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        hash = [-1] * 256
        left, right, maximum = 0, 0, 0
        while right < n:
            if hash[ord(s[right])] != -1:
                left = max(hash[ord(s[right])] + 1, left)
            current_length = right - left + 1
            maximum = max(current_length, maximum)
            hash[ord(s[right])] = right
            right += 1
        return maximum
