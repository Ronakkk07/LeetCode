class Solution:
    # TC - O(4^N * N), SC - O(N)
    def __init__(self):
        self.map = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    def function(self, index, digits, current, ans):
        if index == len(digits):
            ans.append(current)
            return 
        s = self.map[int(digits[index])]
        for char in s:
            self.function(index + 1, digits, current + char, ans)

    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        if not digits:
            return ans
        self.function(0, digits, "", ans)
        return ans

        # # Backtrack/Recursion
        # # TC - no. of combinations O(n*4**n)
        # res =[]
        # digitsToChar = {
        #     "2": "abc",
        #     "3": "def",
        #     "4": "ghi",
        #     "5": "jkl",
        #     "6": "mno",
        #     "7": "qprs",
        #     "8": "tuv",
        #     "9": "wxyz"
        # }
        # def backtrack(i, current_str):
        #     if len(current_str) == len(digits):
        #         res.append(current_str)
        #         return
        #     for c in digitsToChar[digits[i]]:
        #         backtrack(i+1, current_str + c)
        # if digits:
        #     backtrack(0, "")
        # return res