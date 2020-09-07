"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Follow up:

Your algorithm should run in O(n) time and uses constant extra space.
"""
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # put number in right place
        for i in range(len(nums)):
            while nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        for i in range(len(nums)):
            if nums[i] >= len(nums) or nums[i] < 0:
                nums[i] = 0
        for  i in range(len(nums)):
            nums[nums[i] % len(nums)] += len(nums)
        for i in range(len(nums)):
            if nums[i] // len(nums) == 0:
                return i
        return len(nums)