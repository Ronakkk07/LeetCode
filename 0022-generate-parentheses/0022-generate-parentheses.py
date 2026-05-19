class Solution:
    #Time Complexity: O(4n / √n), where n is the number of pairs of parentheses. The number of valid balanced parentheses strings is given by the nth Catalan number. Since each valid combination has length 2n and we generate only valid sequences through backtracking, the total time required is proportional to the number of valid combinations multiplied by their length.

# Space Complexity: O(4n / √n). The dominant space usage comes from storing all valid combinations. Although the recursion stack uses O(n) space, the output storage requires space proportional to the total number of valid combinations (Catalan number) times their length.

# The number of valid balanced parentheses combinations for n pairs is given by the nth Catalan number, defined as Cn = (1 / (n + 1)) × (2n choose n). Asymptotically, the Catalan number grows as 4n / (n3/2 √π). Since each valid string has length 2n, multiplying by n gives the overall complexity bound used above.
    def generate(self, open_count, close_count, n, current, ans):
        if open_count == close_count == n:
            ans.append(current)
            return
        
        if open_count < n:
            self.generate(open_count + 1, close_count, n, current + '(', ans)
        if close_count < open_count:
            self.generate(open_count, close_count + 1, n, current + ')', ans)

    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.generate(0, 0, n, '', ans)
        return ans