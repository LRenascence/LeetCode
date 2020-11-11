"""
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

 

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
"""

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        result = []
        lastLetterIndex = {}
        for index, letter in enumerate(s):
            lastLetterIndex[letter] = index
        for index, letter in enumerate(s):
            if letter not in result:
                while result and letter < result[-1] and lastLetterIndex[result[-1]] > index:
                    result.pop()
                result.append(letter)
        return "".join(result)