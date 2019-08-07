"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        needSwap = False
        i = len(nums) - 1
        while i > 0:
            if nums[i - 1] < nums[i]:
                needSwap = True
                break
            i -= 1
        if needSwap:
            i = i - 1
            j = len(nums) - 1
            while j > i:
                if nums[j] > nums[i]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
                    break
                j -= 1
            i = i + 1
        j = len(nums) - 1
        while i < j:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i += 1
            j -= 1
