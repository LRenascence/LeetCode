"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
Note that the row index starts from 0.
In Pascal's triangle, each number is the sum of the two numbers directly above it.
Example:
Input: 3
Output: [1,3,3,1]
Follow up:
Could you optimize your algorithm to use only O(k) extra space?
"""
class Solution:
    def getRow(self, rowIndex: 'int') -> 'List[int]':
        if rowIndex == 0:
            return [1]
        index = 1
        rList = [1]
        while index <= rowIndex:
            curList = []
            for j in range(index + 1):
                if j == 0:
                    curList.append(rList[0])
                elif j == index:
                    curList.append(rList[-1])
                else:
                    curList.append(rList[j - 1] + rList[j])
            rList = curList
            index += 1
        return rList