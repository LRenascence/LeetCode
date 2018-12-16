"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
Example 1:
Input: [2,2,1]
Output: 1
Example 2:
Input: [4,1,2,1,2]
Output: 4
"""
# hash table solution, normal solution
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashTable = {}
        for i in nums:
            if i in hashTable:
                hashTable.pop(i)
            else:
                hashTable[i] = 1
        return hashTable.popitem()[0]
# math solution, cool solution
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2 * sum(set(nums)) - sum(nums)
# bit solution. coolest solution, O(1) memory
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rValue = 0
        for i in nums:
            rValue ^= i
        return rValue