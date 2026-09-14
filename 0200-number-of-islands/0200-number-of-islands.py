from collections import deque
class Solution:
    def __init__(self):
        self.delRow = [-1, 0, 1, 0]
        self.delCol = [0, 1, 0, -1]

    def isValid(self, i, j, n, m):
        if i < 0 or i >= n:
            return False
        if j < 0 or j >= m:
            return False
        return True
    
    def bfs(self, i, j, vis, grid, n, m):
        vis[i][j] = True
        q = deque()
        q.append((i, j))
        while q:
            row, col = q.popleft()
            for i in range(4):
                    newRow = row + self.delRow[i]
                    newCol = col + self.delCol[i]
                    if (self.isValid(newRow, newCol, n, m) and grid[newRow][newCol] == '1' and not vis[newRow][newCol]):
                        vis[newRow][newCol] = True
                        q.append((newRow, newCol))

    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        vis = [[False]*m for _ in range(n)]
        count = 0
        for i in range(n):
            for j in range(m):
                if not vis[i][j] and grid[i][j] == '1':
                    count += 1
                    self.bfs(i, j, vis, grid, n, m)
        return count
        