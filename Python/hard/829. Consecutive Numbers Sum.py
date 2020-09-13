"""
Given a positive integer N, how many ways can we write it as a sum of consecutive positive integers?

Example 1:

Input: 5
Output: 2
Explanation: 5 = 5 = 2 + 3
Example 2:

Input: 9
Output: 3
Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
Example 3:

Input: 15
Output: 4
Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
"""

class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        index = 1
        result = 0
        while N > index * (index - 1) // 2:
            if (N - (index * (index - 1)) // 2) % index == 0:
                result += 1
            index += 1
        return result