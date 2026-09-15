class Solution:
    def dfs(self, node, adj, visited, pathVisited, order):
        visited[node] = True
        pathVisited[node] = True
        for it in adj[node]:
            if pathVisited[it]:
                return True
            elif not visited[it]:
                if self.dfs(it, adj, visited, pathVisited, order):
                    return True
        pathVisited[node] = False
        order.append(node)

        return False
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj[b].append(a)
        visited = [False] * numCourses
        pathVisited = [False] * numCourses
        order = []
        for i in range(numCourses):
            if not visited[i]:
                if self.dfs(i, adj, visited, pathVisited, order):
                    return []
        order.reverse()
        return order
        