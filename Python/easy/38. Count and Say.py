"""
The count-and-say sequence is the sequence of integers with the first five terms as following:
1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
Note: Each term of the sequence of integers will be represented as a string.
Example 1:
Input: 1
Output: "1"
Example 2:
Input: 4
Output: "1211"
"""
# Using recursion
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        preStr = self.countAndSay(n - 1)
        returnStr = ""
        i = 0
        j = 0
        while True:
            outOfIndex = False
            while preStr[i] == preStr[j]:
                j += 1
                if j == len(preStr):
                    outOfIndex = True
                    break
            num = j - i
            returnStr += str(num) + preStr[i]
            i = j
            if outOfIndex:
                return returnStr

# Not using recursion
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        preStr = "1"
        while n > 1:
            postStr = ""
            i = 0
            j = 0
            outOfIndex = False
            while not outOfIndex:
                while preStr[i] == preStr[j]:
                    j += 1
                    if j == len(preStr):
                        outOfIndex = True
                        break
                num = j - i
                postStr += str(num) + preStr[i]
                i = j
            n -= 1
            preStr = postStr
        return preStr
