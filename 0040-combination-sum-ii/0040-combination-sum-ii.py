class Solution:
    def function(self, index, n, current, candidates, target, ans):
        if target == 0:
            ans.append(current[:])
            return
        if target < 0 or index == n:
            return
        current.append(candidates[index])
        self.function(index + 1, n, current, candidates, target - candidates[index], ans)
        current.pop()
        for i in range(index+1, n):
            if candidates[i] != candidates[index]:
                self.function(i, n, current, candidates, target, ans)
                break
        
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        self.function(0, len(candidates), [], candidates, target, ans)
        return ans