class Solution:
    def __init__(self):
        self.delRow = [-1, 0 , 1, 0]
        self.delCol = [0, 1, 0, -1]

    def isValid(self, i, j, n, m):
        if i < 0 or i >= n:
            return False
        if j < 0 or j >= m:
            return False
        return True

    def dfs(self, row, coln, vis, board, n, m):
        vis[row][coln] = True

        for i in range(4):
            nRow = row + self.delRow[i]
            nColn = coln + self.delCol[i]

            if (self.isValid(nRow, nColn, n, m) and board[nRow][nColn] == 'O' and not vis[nRow][nColn]):
                self.dfs(nRow, nColn, vis, board, n, m)


    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        vis = [[False] * m for _ in range(n)]

        for i in range(m):
            #First Row
            if board[0][i] == 'O' and not vis[0][i]:
                self.dfs(0, i, vis, board, n, m)
            #Last Row
            if board[n-1][i] == 'O' and not vis[n-1][i]:
                self.dfs(n-1, i, vis, board, n, m)
        for j in range(n):
            #First Coln
            if board[j][0] == 'O' and not vis[j][0]:
                self.dfs(j, 0, vis, board, n, m)
            #Last Coln
            if board[j][m-1] == 'O' and not vis[j][m-1]:
                self.dfs(j, m-1, vis, board, n, m)

        for i in range(n):
            for j in range(m):
                if (board[i][j] == 'O' and not vis[i][j]):
                    board[i][j] = 'X'
        return board

        
        