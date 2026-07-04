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
    
    def dfs(self, row, col, ans, image, color, initialcolor):
        ans[row][col] = color
        n = len(image)
        m = len(image[0])
        for i in range(4):
            nRow = row + self.delRow[i]
            nCol = col + self.delCol[i]
            if (self.isValid(nRow, nCol, n, m) and image[nRow][nCol] == initialcolor and ans[nRow][nCol] != color):
                self.dfs(nRow, nCol, ans, image, color, initialcolor)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        initialcolor = image[sr][sc]
        ans = [row[:] for row in image] # To store the updated image
        self.dfs(sr, sc, ans, image, color, initialcolor)
        return ans
        