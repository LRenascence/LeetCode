"""
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
"""
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result = [0] * len(T)
        nextT = [float('inf')] * 102
        for i in range(len(T) - 1, -1, -1):
            warmer = float('inf')
            for j in range(T[i] + 1, 102):
                if nextT[j] < warmer:
                    warmer = nextT[j]
            if warmer < float('inf'):
                result[i] = warmer - i
            nextT[T[i]] = i
        return result
            
# using stack
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result = [0] * len(T)
        stackT = []
        for i in range(len(T) - 1, -1, -1):
            while stackT and T[i] >= T[stackT[-1]]:
                stackT.pop()
            if stackT:
                result[i] = stackT[-1] - i
            stackT.append(i)
        return result
            