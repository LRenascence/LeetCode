"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
"""
class Solution:
    def generate(self, numRows: 'int') -> 'List[List[int]]':
        rList = []
        for i in range(1, numRows + 1):
            if not rList:
                rList.append([1])
            else:
                curList = []
                for j in range(i):
                    if j == 0:
                        curList.append(rList[i - 2][0])
                    elif j == i - 1:
                        curList.append(rList[i - 2][i - 2])
                    else:
                        curList.append(rList[i - 2][j- 1] + rList[i - 2][j])
                rList.append(curList)
        return rList