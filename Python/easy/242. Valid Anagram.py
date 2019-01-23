"""
Given two strings s and t , write a function to determine if t is an anagram of s.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.
Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""


# using one dict only
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        charDict = [0] * 26
        for i in range(len(s)):
            charDict[ord(s[i]) - ord('a')] += 1
            charDict[ord(t[i]) - ord('a')] -= 1
        for i in charDict:
            if i != 0:
                return False
        return True