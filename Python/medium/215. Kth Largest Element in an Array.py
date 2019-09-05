"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]

# use quick selcet avg O(N)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelect(nums, 0, len(nums) - 1, k - 1)
    
    def quickSelect(self, nums, l, r, k):
        pivot = (l + r) // 2
        pivotValue = nums[pivot]
        nums[r], nums[pivot] = nums[pivot], nums[r]
        storeIndex = l
        for i in range(l, r):
            if nums[i] > pivotValue:
                nums[i], nums[storeIndex] = nums[storeIndex], nums[i]
                storeIndex += 1
        nums[r], nums[storeIndex] = nums[storeIndex], nums[r]
        if storeIndex == k:
            return nums[k]
        if storeIndex > k:
            return self.quickSelect(nums, l, storeIndex - 1, k)
        else:
            return self.quickSelect(nums, storeIndex + 1, r, k)