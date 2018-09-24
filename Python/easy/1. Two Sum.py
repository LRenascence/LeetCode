#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author Renascecne

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

# First attempt: time limit exceeded
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        resultList = []
        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                if nums[i] + nums[j] == target:
                    resultList.append(i)
                    resultList.append(j)
                    return resultList
        return resultList

# It's add operation, if I sort the list first, it can save time. However it need number indices, so I need dictionary.
# Actually, it's still O(n2) complexity.
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            dict[i] = nums[i]

        resultList = []
        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                if nums[i] + nums[j] == target:
                    resultList.append(i)
                    resultList.append(j)
                    return resultList
        return resultList

# However, still using dictionary, it can be done with O(n), just use dictionary to store the complement and index.
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict:
                return [dict[nums[i]],i]
            dict[target - nums[i]] = i
        return []