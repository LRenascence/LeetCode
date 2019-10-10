"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic = {}
        curSum = 0
        res = 0
        for i in nums:
            curSum += i
            curDist = curSum - k
            if curDist in dic:
                res += dic[curDist]
            if curSum == k:
                res += 1
            dic[curSum] = dic.get(curSum, 0) + 1
        return res