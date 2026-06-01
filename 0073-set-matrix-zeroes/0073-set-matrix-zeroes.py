class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        index = []
        row = len(matrix)
        column = len(matrix[0])
        for i in range(row):
            for j in range(column):
                if matrix[i][j] == 0:
                    index.append((i,j))
        for i,j in index:
            r,c = 0, 0
            while r < row:
                matrix[r][j] = 0
                r += 1
            while c < column:
                matrix[i][c] = 0
                c += 1
            
        