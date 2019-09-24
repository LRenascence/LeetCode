"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
# use dict and sort
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kDict = {}
        res = []
        for i in nums:
            kDict[i] = kDict.get(i, 0) + 1
        kDict = sorted(kDict.items(), key=lambda item:item[1], reverse = True)
        for i in kDict:
            res.append(i[0])
            k -= 1
            if k == 0:
                return res

# use dict and bucket
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kDict = {}
        bucket = [[] for i in range(len(nums))]
        res = []
        for i in nums:
            kDict[i] = kDict.get(i, 0) + 1
        for i in kDict:
            bucket[kDict[i] - 1].append(i)
        for i in range(len(bucket) - 1, -1, -1):
            for j in range(len(bucket[i])):
                res.append(bucket[i].pop(0))
                if len(res) == k:
                    return res
        
# use dict and bucket, optimization version
# don't create too many space at the first
# only extend the bucket when needed
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kDict = {}
        bucket = [[]]
        res = []
        for i in nums:
            kDict[i] = kDict.get(i, 0) + 1
        for i in kDict:
            while kDict[i] >= len(bucket):
                bucket.append([])
            bucket[kDict[i]].append(i)
        for i in range(len(bucket) - 1, -1, -1):
            for j in range(len(bucket[i])):
                res.append(bucket[i].pop(0))
                if len(res) == k:
                    return res