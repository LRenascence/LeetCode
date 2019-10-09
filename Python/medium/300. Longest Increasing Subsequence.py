"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""

# binary search, O(nlogn)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LISlist = []
        for x in nums:
            i, j = 0, len(LISlist)
            while i != j:
                m = (i + j) // 2
                if LISlist[m] < x:
                    i = m + 1
                else:
                    j = m
            if i == len(LISlist):
                LISlist.append(x)
            else:
                LISlist[i] = x
        return len(LISlist)

# binary search version 2, no big change
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LISlist = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) // 2
                if LISlist[m] < x:
                    i = m + 1
                else:
                    j = m
            LISlist[i] = x
            size = max(i + 1, size)
        return size

# dp solution, O(n2)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        DPlst = [1] * len(nums)
        res = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    DPlst[i] = max(DPlst[i], DPlst[j] + 1)
            res = max(res, DPlst[i])
        return res