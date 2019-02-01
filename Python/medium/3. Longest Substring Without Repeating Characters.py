"""
Given a string, find the length of the longest substring without repeating characters.
Example 1:
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

# O(2*n)
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = right = maxLength = 0
        charSet = set()
        while right < len(s):
            if s[right] not in charSet:
                charSet.add(s[right])
                maxLength = max(maxLength, right - left + 1)
                right += 1
            else:
                charSet.remove(s[left])
                left += 1
        return maxLength

# O(n)
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = right = maxLength = 0
        charDict = {}
        while right < len(s):
            if s[right] not in charDict:
                charDict[s[right]] = right
            if charDict[s[right]] < right:
                left = max(left, charDict[s[right]] + 1)
                charDict[s[right]] = right
            right += 1
            maxLength = max(maxLength, right - left)
        return maxLength
# maybe more fast
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = right = maxLength = 0
        charList = [-1] * 256
        while right < len(s):
            left = max(left, charList[ord(s[right])] + 1)
            charList[ord(s[right])] = right
            right += 1
            maxLength = max(maxLength, right - left)
        return maxLength