from collections import deque
class Solution:
    def bfs(self, start, color, graph):
        q = deque([start])
        color[start] = 0
        while q:
            node = q.popleft()
            for it in graph[node]:
                if color[it] == -1:
                    color[it] = 1 - color[node]
                    q.append(it)
                elif color[it] == color[node]:
                    return False
        return True


    def isBipartite(self, graph: List[List[int]]) -> bool:
        # linear graph, even cycle graph - bipartite
        # graph with odd length cycle - not bipartite
        V = len(graph)
        color = [-1] * V
        for i in range(V):
            if color[i] == -1:
                if self.bfs(i, color, graph) == False:
                    return False
        return True
        
        