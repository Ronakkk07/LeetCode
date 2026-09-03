from collections import deque
class Solution:
    delRow = [-1, 0, 1, 0]
    delCol = [0, 1, 0, -1]

    def isValid(self, i, j, n, m):
        if i < 0 or i>=n: return False
        if j < 0 or j >=m: return False
        return True

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        vis = [[0 for _ in range(m)] for _ in range(n)]
        dist = [[0] * m for _ in range(n)]
        q = deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    q.append(((i,j), 0))
                    vis[i][j] = 1
                else:
                    vis[i][j] = 0
        while q:
            it = q.popleft()
            row, col = it[0]
            steps = it[1]
            dist[row][col] = steps

            for i in range(4):
                nRow = row + self.delRow[i]
                nCol = col + self.delCol[i]
                if (self.isValid(nRow, nCol, n, m) == True and vis[nRow][nCol] == 0):
                    vis[nRow][nCol] = 1
                    q.append(((nRow, nCol), steps + 1))
        return dist
                    

                    
