class Solution:
    # TC - O(N*2**N) 2**N for all possible substring generations and O(N) for each palindrome check
    def ispalindrome(self, s, start, end):
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    def dfs(self, index, s, path, ans):
        if index == len(s):
            ans.append(path[:])
            return
        for i in range(index, len(s)):
            if self.ispalindrome(s, index, i):
                path.append(s[index:i+1])
                self.dfs(i+1, s, path, ans)
                path.pop()

    def partition(self, s: str) -> List[List[str]]:
        ans = []
        self.dfs(0, s, [], ans)
        return ans