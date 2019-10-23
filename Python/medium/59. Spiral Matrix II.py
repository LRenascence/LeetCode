"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""
# simulation
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 1:
            return [[1]]
        res = [[0] * n for i in range(n)]
        i, j = 0, 0
        index = 1
        while res[i][j] == 0:
            while j < n and res[i][j] == 0:
                res[i][j] = index
                index += 1
                j += 1
            j -= 1
            i += 1
            while i < n and res[i][j] == 0:
                res[i][j] = index
                index += 1
                i += 1
            i -= 1
            j -= 1
            while j >= 0 and res[i][j] == 0:
                res[i][j] = index
                index += 1
                j -= 1
            j += 1
            i -= 1
            while i >= 0 and res[i][j] == 0:
                res[i][j] = index
                index += 1
                i -= 1
            i += 1
            j += 1
        return res