#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author Renascecne
"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
"""
# Using string
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        xString = str(x)
        for i in range(0, int(len(xString) / 2)):
            if xString[i] != xString[len(xString) - 1 - i]:
                return False
        return True

#  Without using string
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        reversNumber = 0
        while (x > reversNumber):
            reversNumber *= 10
            reversNumber += x % 10
            x = int(x / 10)
        if x == reversNumber or x == int(reversNumber / 10):
            return True
        else:
            return False