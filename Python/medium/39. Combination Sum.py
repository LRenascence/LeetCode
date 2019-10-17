"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""

# the key is sort the set first
# make sure each result is ascend
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        bfsList = [[target, []]]
        res = []
        while bfsList:
            target, path = bfsList.pop(0)
            if target == 0:
                res.append(path)
                continue
            for i in candidates:
                if i > target:
                    break
                if path and i < path[-1]:
                    continue
                bfsList.append([target - i, path + [i]])
        return res
        