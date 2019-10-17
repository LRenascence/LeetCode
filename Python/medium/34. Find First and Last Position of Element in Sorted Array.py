"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""

# use binary search 3 times
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        # find target
        index = self.binarySearch(nums, target)
        if nums[index] != target:
            return [-1, -1]
        # find left bound
        leftBound = self.binarySearch(nums, target - 0.5)
        # find right bound
        rightBound = self.binarySearch(nums, target + 0.5)
        if nums[rightBound] != target:
            rightBound -= 1
        return [leftBound, rightBound]
    
    def binarySearch(self, nums, target):
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m
        return l

# use find lower bound
# slower than the first
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        leftBound = self.findLowerBound(nums, target)
        rightBound = self.findLowerBound(nums, target + 1) - 1
        if leftBound < len(nums) and nums[leftBound] == target:
            return [leftBound, rightBound]
        return [-1, -1]
    
    def findLowerBound(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l += 1
            else:
                r -= 1
        return l
                