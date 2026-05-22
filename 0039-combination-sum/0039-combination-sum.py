class Solution:
    # Time Complexity: O(K*N(Target/m)), where N is the number of elements, and m is the minimum value among the elements. This is because the algorithm explores an exponential number of possible combinations in the worst case, as elements can be chosen repeatedly to form the target.
    # Space Complexity: O(Target/m), because the deepest recursion and the longest combination both occur when repeatedly choosing the smallest element.
    def function(self, index, n, current, candidates, target, ans):
        if target == 0:
            ans.append(current[:])
            return
        if target < 0 or index == n:
            return
        current.append(candidates[index])
        self.function(index, n, current, candidates, target - candidates[index], ans)
        current.pop()
        self.function(index + 1, n, current, candidates, target, ans)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        self.function(0, len(candidates), [], candidates, target, ans)
        return ans