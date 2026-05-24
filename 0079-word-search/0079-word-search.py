class Solution:
    def function(self, board, i, j, word, index):
        if index == len(word):
            return True
        if i<0 or j<0 or i >= len(board) or j >= len(board[0]) or word[index] != board[i][j]:
            return False
        
        temp = board[i][j]
        board[i][j] = ' '

        ans = (self.function(board, i + 1, j, word, index + 1) or
        self.function(board, i - 1, j, word, index + 1) or
        self.function(board, i, j + 1, word, index + 1) or
        self.function(board, i, j - 1, word, index + 1))

        board[i][j] = temp
        return ans
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        column = len(board[0])
        for i in range(row):
            for j in range(column):
                if board[i][j] == word[0]:
                    if self.function(board, i, j, word, 0):
                        return True
        return False