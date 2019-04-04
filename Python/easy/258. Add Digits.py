"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
             Since 2 has only one digit, return it.
Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""

# easy solution
class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            res = 0
            while num != 0:
                res += num % 10
                num //= 10
            if res < 10:
                return res
            else:
                num = res

# fancy solution
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        else:
            return (num - 1) % 9 + 1