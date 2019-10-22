"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        resList = [0] * (len(num1) + len(num2))
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                pos1, pos2 = i + j, i + j + 1
                mult = int(num1[i]) * int(num2[j])
                sumRes = resList[pos2] + mult
                resList[pos1] += sumRes // 10
                resList[pos2] = sumRes % 10
        index = 0
        while index < len(resList) and resList[index] == 0:
            index += 1
        if index == len(resList):
            return '0'
        res = ''
        for i in range(index, len(resList)):
            res += str(resList[i])
        return res