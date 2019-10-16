"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""
# N-Sum solution
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        self.NSum(nums, target, 4, [], result)
        return result
    
    def NSum(self, nums, k, N, temp, result):
        if N <= 1 or len(nums) < N:
            return
        # two sum
        if N == 2:
            l, r = 0, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == k:
                    result.append(temp + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # unique result
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] < k:
                    l += 1
                else:
                    r -= 1
                        
        # if not two sum, recude N to N - 1
        else:
            for i in range(len(nums) - N + 1):
                # precheck if it can have a result
                if nums[i] * N > k or nums[-1] * N < k:
                    break
                # reduce N to N - 1
                if i == 0 or (nums[i] != nums[i - 1]):
                    self.NSum(nums[i + 1:], k - nums[i], N - 1, temp + [nums[i]], result)
        return