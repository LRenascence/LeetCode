"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result1, result2 = 0, 1
        counter1, counter2 = 0, 0
        for i in nums:
            if result1 == i:
                counter1 += 1
            elif result2 == i:
                counter2 += 1
            elif counter1 == 0:
                result1 = i
                counter1 = 1
            elif counter2 == 0:
                result2 = i
                counter2 = 1
            else:
                counter1 -= 1
                counter2 -= 1
        return [n for n in [result1, result2] if (nums.count(n) > len(nums) // 3)]