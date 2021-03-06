"""
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        isNegative = True if n < 0 else False
        n = abs(n)
        result = 1
        while n > 0:
            temp = x
            m = 1
            while m << 1 < n:
                temp *= temp
                m <<= 1
            result *= temp
            n -= m
        return 1 / result if isNegative else result