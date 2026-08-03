class Solution:
    #SC - O(N) visited array + O(N) Recursion stack space
    # TC - N nodes and N calls for DFS is made O(N) + O(V + 2E) traversal of Graph
    def dfs(self, node, adj, vis):
        vis[node] = 1
        for it in adj[node]:
            if not vis[it]:
                self.dfs(it, adj, vis)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        V = len(isConnected)
        vis = [0] * V
        adj = [[] for _ in range(V)]
        for i in range(V):
            for j in range(V):
                if isConnected[i][j] == 1 and i != j:
                    adj[i].append(j)
        cnt = 0
        for i in range(V):
            if not vis[i]:
                cnt += 1
                self.dfs(i, adj, vis)
        return cnt
