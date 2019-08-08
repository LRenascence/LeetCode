"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(curList):
            if len(curList) == len(nums):
                result.append(curList)
                return
            for i in nums:
                if i in curList:
                    continue
                dfs(curList + [i])

        dfs([])
        return result