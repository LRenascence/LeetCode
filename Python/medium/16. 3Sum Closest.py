"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        N = len(nums)
        if N < 3:
            return 0
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        minDist = abs(target - result)
        for i in range(N):
            L, R = i + 1, N - 1
            while L < R:
                curSum = nums[i] + nums[L] + nums[R]
                curDist = abs(target - curSum)
                if curSum == target:
                    return target
                else:
                    if minDist > curDist:
                        result = curSum
                        minDist = curDist
                if curSum < target:
                    L += 1
                else:
                    R -= 1
        return result