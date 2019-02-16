"""
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false

"""


class Solution:
    def isPowerOfTwo(self, n: 'int') -> 'bool':
        if n <= 0:
            return False
        s = bin(n)
        count = 0
        for i in s:
            if i == '1':
                count += 1
        if count == 1:
            return True
        else:
            return False
