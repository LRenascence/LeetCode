"""
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.
"""

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # merge sort
        def mergeSort(lst):
            if len(lst) <= 1:
                return
            l, mid, r = 0, len(lst) // 2, 0
            left = lst[:mid]
            right = lst[mid:]
            mergeSort(left)
            mergeSort(right)
            index = 0
            while l < len(left) and r < len(right):
                if str(left[l]) + str(right[r]) > str(right[r]) + str(left[l]):
                    lst[index] = left[l]
                    l += 1
                else:
                    lst[index] = right[r]
                    r += 1
                index += 1
            while l < len(left):
                lst[index] = left[l]
                l += 1
                index += 1
            while r < len(right):
                lst[index] = right[r]
                r += 1
                index += 1
            return
        mergeSort(nums)
        result = ""
        for num in nums:
            result += str(num)
        index = 0
        while result[index] == '0' and index + 1 < len(result) and result[index + 1] == '0':
            index += 1
        result = result[index:]
        return result