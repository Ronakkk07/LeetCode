class Solution:
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