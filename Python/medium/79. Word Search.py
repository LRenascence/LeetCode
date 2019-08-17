"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""

# recursive dfs
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(i, j, board, word):
                    return True
        return False

    def dfs(self, i, j, board, word):
        if len(word) == 0:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0]:
            return False
        temp = board[i][j]
        board[i][j] = '#'
        res = self.dfs(i - 1, j, board, word[1:]) or self.dfs(i + 1, j, board, word[1:]) or self.dfs(i, j - 1, board,
            word[1:]) or self.dfs(i, j + 1, board, word[1:])
        board[i][j] = temp
        return res