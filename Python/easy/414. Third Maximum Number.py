"""
Given a non-empty array of integers, return the third maximum number in this array.
If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
"""


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        biggest = None
        bigger = None
        big = None
        for i in nums:
            if i == biggest or i == bigger or i == big:
                continue
            elif biggest is None or i > biggest:
                big = bigger
                bigger = biggest
                biggest = i
            elif bigger is None or i > bigger:
                big = bigger
                bigger = i
            elif big is None or i > big:
                big = i
        return big if big is not None else biggest
