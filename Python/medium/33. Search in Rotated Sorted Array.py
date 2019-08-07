"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        # find the smallest value first
        N = len(nums)
        l, r = 0, N - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        # use binary search to find the target
        begin = l
        l, r = 0, N
        print(begin)
        while l <= r:
            mid = (l + r) // 2
            trueMid = (mid + begin) % N
            if nums[trueMid] == target:
                return trueMid
            elif nums[trueMid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1