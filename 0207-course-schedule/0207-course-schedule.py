class Solution:
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

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for it in prerequisites:
            u = it[0]
            v = it[1]
            adj[v].append(u)

        topo = self.topoSort(numCourses, adj)
        if len(topo) < numCourses:
            return False
        return True
        