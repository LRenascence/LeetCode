"""
reated by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
"""

# the idea is from https://leetcode.com/problems/game-of-life/discuss/73223/Easiest-JAVA-solution-with-explanation
"""
[2nd bit, 1st bit] = [next state, current state]

- 00  dead (next) <- dead (current)
- 01  dead (next) <- live (current)  
- 10  live (next) <- dead (current)  
- 11  live (next) <- live (current) 
"""

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        M, N = len(board), len(board[0])
        
        def neighbor(x, y):
            live = 0
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    if x + i >= 0 and x + i < M and y + j >= 0 and y + j < N:
                        live += board[x + i][y + j] & 1
            live -= board[x][y] & 1
            return live
        
        for i in range(M):
            for j in range(N):
                liveNeighbor = neighbor(i, j)
                if (liveNeighbor == 2 or liveNeighbor == 3) and board[i][j] == 1:
                    board[i][j] = 3
                elif liveNeighbor == 3 and board[i][j] == 0:
                    board[i][j] = 2
        
        for i in range(M):
            for j in range(N):
                board[i][j] >>= 1
        
        return