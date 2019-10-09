"""
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:
Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.
Example 2:
Input: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
Note:
N is in range [1,200].
M[i][i] = 1 for all students.
If M[i][j] = 1, then M[j][i] = 1.
"""

# use set operation
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        res = []
        for i in range(len(M)):
            curSet = set()
            for j in range(len(M[0])):
                if M[i][j] == 1:
                    curSet.add(j)
            res.append(curSet)
        needUnion = True
        while needUnion:
            needUnion = False
            for i in range(len(res)):
                for j in range(i + 1, len(res)):
                    if res[i].intersection(res[j]):
                        res.append(res[i].union(res[j]))
                        res.pop(j)
                        res.pop(i)
                        needUnion = True
                        break
        return len(res)

# use dfs
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        res = 0
        visited = [0] * len(M)
        def dfs(j):
            dfsList = [j]
            while dfsList:
                curP = dfsList.pop()
                for x in range(len(M[0])):
                    if M[curP][x] == 1 and visited[x] == 0:
                        visited[x] = 1
                        dfsList.append(x)
        for i in range(len(M)):
            if visited[i] == 0:
                dfs(i)
                res += 1
        return res

