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
    
    def bfs(self, grid, q, vis, n, m):
        while q:
            cell = q.popleft()
            row, col = cell
            for i in range(4):
                nRow = row + self.delRow[i]
                nCol = col + self.delCol[i]
                if (self.isValid(nRow, nCol, n, m) and grid[nRow][nCol] == 1 and vis[nRow][nCol] == False):
                    vis[nRow][nCol] = True
                    q.append((nRow, nCol))
                    
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        vis = [[False] * m for _ in range(n)]
        q = deque()

        for i in range(n):
            for j in range(m):
                if ((i == 0 or  i == n-1 or j == 0 or j == m-1) and grid[i][j] == 1):
                    vis[i][j] = True
                    q.append((i, j))
        self.bfs(grid, q, vis, n, m) 
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not vis[i][j]:
                    count += 1
        return count
        