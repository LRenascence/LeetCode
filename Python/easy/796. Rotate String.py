"""
We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position.
For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false
Note:

A and B will have length at most 100.
"""

# sim rotate
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if A == B:
            return True

        for i in range(len(A)):
            # sim rotate
            A = A[1:] + A[0]
            if A == B:
                return True

        return False

# smarter
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        A = A + A
        if B in A:
            return True
        return False