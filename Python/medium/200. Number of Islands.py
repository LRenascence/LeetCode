"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""
# DFS recurse
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        def dfs(i, j):
            if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]):
                if grid[i][j] == "1":
                    grid[i][j] = "2"
                    dfs(i - 1, j)
                    dfs(i + 1, j)
                    dfs(i, j + 1)
                    dfs(i, j - 1)
            return None
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1
        return res