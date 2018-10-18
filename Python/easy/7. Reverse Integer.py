"""Given a 32-bit signed integer, reverse digits of an integer.
Example 1:
Input: 123
Output: 321
Example 2:
Input: -123
Output: -321
Example 3:
Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""
# My solution, not right exactly
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < -2 ** 31 or x > 2 ** 31 - 1:
            return 0
        flag = False
        if x < 0:
            x = -x
            flag = True
        digitalLevel = 1
        returnData = 0
        returnDataLevel = 1
        while x / digitalLevel >=10:
            digitalLevel *= 10
        while x >= 10:
            returnData += int(x / digitalLevel) * returnDataLevel
            x %= digitalLevel
            while x / digitalLevel < 1:
                digitalLevel /= 10
                returnDataLevel *= 10
                if x ==0:
                    break
        returnData += int(x * returnDataLevel)
        if flag:
            returnData = -returnData
        if returnData < -2**31 or returnData > 2**31-1:
            return 0
        return returnData

# Solution
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        returnData = 0
        maxInt = 2 ** 31 - 1
        minInt = -2 ** 31
        while x != 0:
            if x > 0:
                pop = int(x % 10)
            else:
                pop = int(x % -10)
            x = int(x / 10)
            if returnData > maxInt / 10 or (returnData == maxInt / 10 and pop > 7):
                return 0
            if returnData < minInt / 10 or (returnData == minInt / 10 and pop < -8):
                return 0
            returnData = returnData * 10 + pop
        return returnData