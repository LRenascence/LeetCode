"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
Examples:
s = "leetcode"
return 0.
s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        indexDict = {}
        for i in range(len(s)):
            if s[i] not in indexDict:
                indexDict[s[i]] = i
            else:
                indexDict[s[i]] = len(s)
        minIndex = len(s)
        for i in indexDict:
            if indexDict[i] < minIndex:
                minIndex = indexDict[i]
        if minIndex == len(s):
            return -1
        else:
            return minIndex