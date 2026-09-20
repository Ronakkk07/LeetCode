class Solution:
    def dfs(self, node, graph, vis, pathvis, check):
        vis[node] = True
        pathvis[node] = True
        check[node] = False
        for it in graph[node]:
            if not vis[it]:
                if self.dfs(it, graph, vis, pathvis, check):
                    check[node] = False
                    return True
            elif pathvis[it]:
                check[node] = False
                return True
        check[node] = True
        pathvis[node] = False
        return False

    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        V = len(graph)
        vis = [False] * V
        pathvis = [False] * V
        check = [False] * V 
        for i in range(V):
            if not vis[i]:
                self.dfs(i, graph, vis, pathvis, check)
        ans = []
        for i in range(V):
            if check[i]:
                ans.append(i)
        return ans      