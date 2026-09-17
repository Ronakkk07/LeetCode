class Solution:
    # Detect cycle in directed graph extended version
    # def dfs(self, node, adj, visited, pathVisited, order):
    #     visited[node] = True
    #     pathVisited[node] = True
    #     for it in adj[node]:
    #         if pathVisited[it]:
    #             return True
    #         elif not visited[it]:
    #             if self.dfs(it, adj, visited, pathVisited, order):
    #                 return True
    #     pathVisited[node] = False
    #     order.append(node)

    #Topo sort (Kahn's Algorithm)
    def topoSort(self, V, adj):
        inDegree = [0] * V
        for i in range(V):
            for it in adj[i]:
                inDegree[it] += 1
        ans = []
        q = deque()
        for i in range(V):
            if inDegree[i] == 0:
                q.append(i)
        while q:
            node = q.popleft()
            ans.append(node)
            for it in adj[node]:
                inDegree[it] -= 1
                if inDegree[it] == 0:
                    q.append(it)
        return ans

        return False
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # adj = [[] for _ in range(numCourses)]
        # for a, b in prerequisites:
        #     adj[b].append(a)
        # visited = [False] * numCourses
        # pathVisited = [False] * numCourses
        # order = []
        # for i in range(numCourses):
        #     if not visited[i]:
        #         if self.dfs(i, adj, visited, pathVisited, order):
        #             return []
        # order.reverse()
        # return order

        adj = [[] for _ in range(numCourses)]
        for u,v in prerequisites:
            adj[v].append(u)
        topo = self.topoSort(numCourses, adj)
        if len(topo) < numCourses:
            return []
        return topo
        