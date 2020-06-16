"""
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:

Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
 

Constraints:

The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
"""

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # recursive solution
        index = len(nums) - 1
        self.dpMem = {}
        return self.dp(nums, S, index)
    
    def dp(self, nums, S, index):
        if (index, S) in self.dpMem:
            return self.dpMem[(index, S)]
        # base case
        if index < 0 and S == 0:
            return 1
        if index < 0:
            return 0
        # decision case
        positive = self.dp(nums, S - nums[index], index - 1)
        negative = self.dp(nums, S + nums[index], index - 1)
        self.dpMem[(index, S)] = positive + negative
        return positive + negative