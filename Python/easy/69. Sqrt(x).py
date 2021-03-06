"""
Implement int sqrt(int x).
Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
Example 1:
Input: 4
Output: 2
Example 2:
Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
"""

# binary search, in discussion, there is Newton method.
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1:
            return 1
        left = 0
        right = x
        mid = int(left + (right - left) / 2)
        while True:
            if mid * mid < x:
                if (mid + 1) * (mid + 1) > x:
                    return mid
                else:
                    left = mid
            elif mid * mid > x:
                right = mid
            else:
                return mid
            mid = int(left + (right - left) / 2)