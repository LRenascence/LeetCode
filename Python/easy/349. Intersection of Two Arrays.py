"""
Given two arrays, write a function to compute their intersection.
Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:
Each element in the result must be unique.
The result can be in any order.
"""
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        numDict = {}
        rList = []
        for i in nums1:
            if i not in numDict:
                numDict[i] = 1
        for i in nums2:
            if i in numDict and numDict[i] == 1:
                numDict[i] = 0
                rList.append(i)
        return rList

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        num1Set = set(nums1)
        rList = []
        for i in nums2:
            if i in num1Set:
                rList.append(i)
                num1Set.remove(i)
        return rList